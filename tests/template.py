import os.path
import warnings
import ast
import json

from tests.nodes import convert_node


class Template(object):
    def __init__(self, pattern):
        self.pattern = TemplateTransformer.load(pattern)

    def process(self, code, raw=False):
        tree = ast.parse(code) if isinstance(code, str) else code

        nodes = []
        for node in ast.walk(tree):
            if isinstance(node, type(self.pattern)) and is_ast_equal(
                node, self.pattern
            ):
                if not raw:
                    nodes.append(convert_node(node))
                else:
                    nodes.append(node)

        return nodes

    def process_file(self, filename):
        if isinstance(filename, str):
            with open(filename, "rb") as file:
                tree = ast.parse(file.read())
        else:
            tree = ast.parse(filename.read())
        yield from self.query(tree)

    def filter_subdirs(self, dirnames):
        dirnames[:] = [d for d in dirnames if d != "build"]

    def process_directory(self, directory):
        for dirpath, dirnames, filenames in os.walk(directory):
            self.filter_subdirs(dirnames)

            for filename in filenames:
                if filename.endswith((".py", ".pyw")):
                    filepath = os.path.join(dirpath, filename)
                    try:
                        for match in self.query_file(filepath):
                            yield filepath, match
                    except SyntaxError as e:
                        warnings.warn(
                            "Failed to parse {}:\n{}".format(filepath, e))


class TemplateTransformer(ast.NodeTransformer):

    __WILDCARD_NAME = "__past_wildcard"
    __MULTIWILDCARD_NAME = "__past_multiwildcard"

    @classmethod
    def load(cls, pattern):
        pattern = pattern.replace("??", cls.__MULTIWILDCARD_NAME).replace(
            "?", cls.__WILDCARD_NAME
        )
        transformed = ast.parse(pattern).body[0]

        if isinstance(transformed, ast.Expr):
            transformed = transformed.value
        if isinstance(transformed, (ast.Attribute, ast.Subscript)):
            del transformed.ctx

        return cls().visit(transformed)

    def must_exist(self, node, path):
        if (node is None) or (node == []):
            raise TemplateMismatch(path, node, "non empty")

    def must_not_exist(self, node, path):
        if (node is not None) and (node != []):
            raise TemplateMismatch(path, node, "empty")

    def visit_Name(self, node):
        if node.id == self.__WILDCARD_NAME:
            return self.must_exist
        elif node.id == self.__MULTIWILDCARD_NAME:
            return self.must_exist

        return NameOrAttr(node.id)

    def transform_wildcard(self, node, attrname):
        if getattr(node, attrname, None) in (
            self.__WILDCARD_NAME,
            self.__MULTIWILDCARD_NAME,
        ):
            setattr(node, attrname, self.must_exist)

    def transform_wildcard_body(self, node, attrname):
        body = getattr(node, attrname, [])

        def _is_multiwildcard(n):
            return is_ast_equal(
                n, ast.Expr(value=ast.Name(id=self.__MULTIWILDCARD_NAME))
            )

        if len(body) == 1 and _is_multiwildcard(body[0]):
            setattr(node, attrname, self.must_exist)
            return

        for i, n in enumerate(body):
            if _is_multiwildcard(n):
                newbody = body[:i] + Middle() + body[i + 1:]
                setattr(node, attrname, newbody)

    def visit_Attribute(self, node):
        self.transform_wildcard(node, "attr")
        return self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.transform_wildcard(node, "name")
        self.transform_wildcard_body(node, "body")
        return self.generic_visit(node)

    visit_ClassDef = visit_FunctionDef

    def visit_arguments(self, node):
        positional_final_wildcard = False
        for i, a in enumerate(node.args):
            if a.arg == self.__MULTIWILDCARD_NAME:
                from_end = len(node.args) - (i + 1)
                if from_end == 0:
                    positional_final_wildcard = True

                args = (
                    self.visit_list(node.args[:i])
                    + Middle()
                    + self.visit_list(node.args[i + 1:])
                )
                break
        else:
            if node.args:
                args = self.visit_list(node.args)
            else:
                args = self.must_not_exist

        defaults = [
            (a.arg, self.visit(d))
            for a, d in zip(node.args[-len(node.defaults):], node.defaults)
            if a.arg not in {self.__WILDCARD_NAME, self.__MULTIWILDCARD_NAME}
        ]

        if node.vararg is None:
            if positional_final_wildcard:
                vararg = None
            else:
                vararg = self.must_not_exist
        else:
            vararg = self.visit(node.vararg)

        kwonly_args_dflts = [
            (self.visit(a), (d if d is None else self.visit(d)))
            for a, d in zip(node.kwonlyargs, node.kw_defaults)
            if a.arg != self.__MULTIWILDCARD_NAME
        ]

        koa_subset = (
            positional_final_wildcard and vararg is None and (
                not node.kwonlyargs)
        ) or any(a.arg == self.__MULTIWILDCARD_NAME for a in node.kwonlyargs)

        if node.kwarg is None:
            if koa_subset:
                kwarg = None
            else:
                kwarg = self.must_not_exist
        else:
            kwarg = self.visit(node.kwarg)

        return DefArgsCheck(
            args=args,
            defaults=defaults,
            vararg=vararg,
            kwonly_args_dflts=kwonly_args_dflts,
            koa_subset=koa_subset,
            kwarg=kwarg,
        )

    def visit_arg(self, node):
        self.transform_wildcard(node, "arg")
        return self.generic_visit(node)

    def visit_If(self, node):
        self.transform_wildcard_body(node, "body")
        self.transform_wildcard_body(node, "orelse")
        return self.generic_visit(node)

    visit_For = visit_While = visit_If

    def visit_Try(self, node):
        self.transform_wildcard_body(node, "body")
        self.transform_wildcard_body(node, "orelse")
        self.transform_wildcard_body(node, "finalbody")
        return self.generic_visit(node)

    def visit_ExceptHandler(self, node):
        self.transform_wildcard(node, "name")
        self.transform_wildcard_body(node, "body")
        return self.generic_visit(node)

    def visit_With(self, node):
        self.transform_wildcard_body(node, "body")
        return self.generic_visit(node)

    def visit_Call(self, node):
        kwargs_are_subset = False
        for i, n in enumerate(node.args):
            if is_ast_equal(n, ast.Name(id=self.__MULTIWILDCARD_NAME)):
                if i + 1 == len(node.args):
                    kwargs_are_subset = True

                node.args = (
                    self.visit_list(node.args[:i])
                    + Middle()
                    + self.visit_list(node.args[i + 1:])
                )

                break

        if kwargs_are_subset or any(
            k.arg == self.__MULTIWILDCARD_NAME for k in node.keywords
        ):
            template_keywords = [
                self.visit(k)
                for k in node.keywords
                if k.arg != self.__MULTIWILDCARD_NAME
            ]

            def kwargs_checker(sample_keywords, path):
                sample_kwargs = {k.arg: k.value for k in sample_keywords}

                for k in template_keywords:
                    if k.arg == self.__MULTIWILDCARD_NAME:
                        continue
                    if k.arg in sample_kwargs:
                        assert_ast_equal(
                            sample_kwargs[k.arg], k.value, path + [k.arg])
                    else:
                        raise TemplateMismatch(
                            path, "(missing)", "keyword arg %s" % k.arg
                        )

            if template_keywords:
                node.keywords = kwargs_checker
            else:
                del node.keywords

        if node.args == []:
            node.args = self.must_not_exist
        if getattr(node, "keywords", None) == []:
            node.keywords = self.must_not_exist
        return self.generic_visit(node)

    def transform_import_names(self, node):
        if len(node.names) == 1 and node.names[0].name == self.__MULTIWILDCARD_NAME:
            del node.names
        else:
            for alias in node.names:
                self.visit_alias(alias)

    def visit_Import(self, node):
        self.transform_import_names(node)
        return node

    def visit_ImportFrom(self, node):
        self.transform_wildcard(node, "module")
        self.transform_import_names(node)
        if node.level == 0:
            del node.level
        return node

    def visit_alias(self, node):
        self.transform_wildcard(node, "name")
        if node.asname is None:
            del node.asname
        else:
            self.transform_wildcard(node, "asname")

    def generic_visit(self, node):
        for field, old_value in ast.iter_fields(node):
            old_value = getattr(node, field, None)
            if isinstance(old_value, list):
                new_values = []
                for value in old_value:
                    if isinstance(value, ast.AST):
                        value = self.visit(value)
                        if value is None:
                            continue
                        elif isinstance(value, list):
                            new_values.extend(value)
                            continue
                    new_values.append(value)

                if not new_values:
                    delattr(node, field)

                old_value[:] = new_values
            elif isinstance(old_value, ast.AST):
                new_node = self.visit(old_value)
                if new_node is None:
                    delattr(node, field)
                else:
                    setattr(node, field, new_node)
        return node

    def visit_list(self, l):
        return [self.visit(n) for n in l]


class NameOrAttr(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "past.NameOrAttr({%r})" % self.name

    def __call__(self, node, path):
        if isinstance(node, ast.Name):
            if node.id != self.name:
                raise TemplatePlainObjMismatch(
                    path + ["id"], node.id, self.name)
        elif isinstance(node, ast.Attribute):
            if node.attr != self.name:
                raise TemplatePlainObjMismatch(
                    path + ["attr"], node.attr, self.name)
        else:
            raise TemplateNodeTypeMismatch(path, node, "Name or Attribute")


class Middle(object):
    def __init__(self, front=None, back=None):
        super(Middle, self).__init__()
        self.front = front or []
        self.back = back or []

    def __radd__(self, other):
        if not isinstance(other, list):
            raise TypeError(
                "Cannot add {} and Middle objects".format(type(other)))
        return Middle(other + self.front, self.back)

    def __add__(self, other):
        if not isinstance(other, list):
            raise TypeError(
                "Cannot add Middle and {} objects".format(type(other)))
        return Middle(self.front, self.back + other)

    def __call__(self, sample_list, path):
        if not isinstance(sample_list, list):
            raise TemplateNodeTypeMismatch(path, sample_list, list)

        if self.front:
            nfront = len(self.front)
            if len(sample_list) < nfront:
                raise TemplateNodeListMismatch(
                    path + ["<front>"], sample_list, self.front
                )
            check_node_list(path, sample_list[:nfront], self.front)
        if self.back:
            nback = len(self.back)
            if len(sample_list) < nback:
                raise TemplateNodeListMismatch(
                    path + ["<back>"], sample_list, self.back
                )
            check_node_list(path, sample_list[-nback:], self.back, -nback)


class TemplateMismatch(AssertionError):
    def __init__(self, path, got, expected):
        self.path = path
        self.expected = expected
        self.got = got

    def __str__(self):
        return ("Mismatch at {}.\n" "Found   : {}\n" "Expected: {}").format(
            format_path(self.path), self.got, self.expected
        )


class TemplateNodeTypeMismatch(TemplateMismatch):
    def __str__(self):
        expected = (
            type(self.expected).__name__
            if isinstance(self.expected, ast.AST)
            else self.expected
        )
        return "At {}, found {} node instead of {}".format(
            format_path(self.path), type(self.got).__name__, expected
        )


class TemplateNodeListMismatch(TemplateMismatch):
    def __str__(self):
        return "At {}, found {} node(s) instead of {}".format(
            format_path(self.path), len(self.got), len(self.expected)
        )


class TemplatePlainListMismatch(TemplateMismatch):
    def __str__(self):
        return ("At {}, lists differ.\nFound   : {}\nExpected: {}").format(
            format_path(self.path), self.got, self.expected
        )


class TemplatePlainObjMismatch(TemplateMismatch):
    def __str__(self):
        return "At {}, found {!r} instead of {!r}".format(
            format_path(self.path), self.got, self.expected
        )


class DefArgsCheck:
    def __init__(self, args, defaults, vararg, kwonly_args_dflts, koa_subset, kwarg):
        self.args = args
        self.defaults = defaults
        self.vararg = vararg
        self.kwonly_args_dflts = kwonly_args_dflts
        self.koa_subset = koa_subset
        self.kwarg = kwarg

    def __repr__(self):
        return (
            "past.DefArgsCheck(args={s.args}, defaults={s.defaults}, "
            "vararg={s.vararg}, kwonly_args_dflts={s.kwonly_args_dflts}, "
            "koa_subset={s.koa_subset}, kwarg={s.kwarg}"
        ).format(s=self)

    def __call__(self, sample_node, path):
        if self.args:
            if isinstance(self.args, list):
                check_node_list(path + ["args"], sample_node.args, self.args)
            else:
                assert_ast_equal(sample_node.args, self.args)

        if self.defaults:
            sample_args_w_defaults = sample_node.args[-len(
                sample_node.defaults):]
            sample_arg_defaults = {
                a.arg: d for a, d in zip(sample_args_w_defaults, sample_node.defaults)
            }
            for argname, dflt in self.defaults:
                try:
                    sample_dflt = sample_arg_defaults[argname]
                except KeyError:
                    raise TemplateMismatch(
                        path + ["defaults", argname], "(missing default)", dflt
                    )
                else:
                    assert_ast_equal(dflt, sample_dflt,
                                     path + ["defaults", argname])

        if self.vararg:
            assert_ast_equal(sample_node.vararg, self.vararg)

        sample_kwonlyargs = {
            k.arg: (k, d)
            for k, d in zip(sample_node.kwonlyargs, sample_node.kw_defaults)
        }

        for template_arg, template_dflt in self.kwonly_args_dflts:
            argname = template_arg.arg
            try:
                sample_arg, sample_dflt = sample_kwonlyargs[argname]
            except KeyError:
                raise TemplateMismatch(
                    path +
                    ["kwonlyargs"], "(missing)", "keyword arg %s" % argname
                )
            else:
                assert_ast_equal(
                    sample_arg, template_arg, path + ["kwonlyargs", argname]
                )
                if template_dflt is not None:
                    assert_ast_equal(
                        sample_dflt, template_dflt, path +
                        ["kw_defaults", argname]
                    )

        if not self.koa_subset:
            template_kwarg_names = {k.arg for k, d in self.kwonly_args_dflts}
            excess_names = set(sample_kwonlyargs) - template_kwarg_names
            if excess_names:
                raise TemplateMismatch(
                    path +
                    ["kwonlyargs"], excess_names, "(not present in template)"
                )

        if self.kwarg:
            assert_ast_equal(sample_node.kwarg, self.kwarg)


def format_path(path):
    formed = path[:1]
    for part in path[1:]:
        if isinstance(part, int):
            formed.append("[%d]" % part)
        else:
            formed.append("." + part)
    return "".join(formed)


def check_node_list(path, sample, template, start_enumerate=0):
    if len(sample) != len(template):
        raise TemplateNodeListMismatch(path, sample, template)

    for i, (sample_node, template_node) in enumerate(
        zip(sample, template), start=start_enumerate
    ):
        if callable(template_node):
            template_node(sample_node, path + [i])
        else:
            assert_ast_equal(sample_node, template_node, path + [i])


def assert_ast_equal(sample, template, path=None):
    if path is None:
        path = ["tree"]

    if callable(template):
        return template(sample, path)

    if not isinstance(sample, type(template)):
        raise TemplateNodeTypeMismatch(path, sample, template)

    for name, template_field in ast.iter_fields(template):
        sample_field = getattr(sample, name)
        field_path = path + [name]

        if isinstance(template_field, list):
            if template_field and (
                isinstance(template_field[0], ast.AST) or callable(
                    template_field[0])
            ):
                check_node_list(field_path, sample_field, template_field)
            else:
                if sample_field != template_field:
                    raise TemplatePlainListMismatch(
                        field_path, sample_field, template_field
                    )

        elif isinstance(template_field, ast.AST):
            assert_ast_equal(sample_field, template_field, field_path)

        elif callable(template_field):
            template_field(sample_field, field_path)

        else:
            if sample_field != template_field:
                raise TemplatePlainObjMismatch(
                    field_path, sample_field, template_field)


def is_ast_equal(sample, template):
    try:
        assert_ast_equal(sample, template)
        return True
    except TemplateMismatch:
        return False


def debug_test_case(node):
    """Print JSON parser nodes

    Arguments:
        node {[type]} -- [description]
    """
    print(json.dumps(node.assign_().n, indent=4)) 
    print(json.dumps(node.for_().n, indent=4)) 
    print(json.dumps(node.returns_call().n, indent=4))


def debug_test_case_class(node, test_method):
    """Print JSON parser nodes for class properties

    Arguments:
        node {[type]} -- [description]
    """
    print(json.dumps(node.def_args_(test_method).n, indent=4))