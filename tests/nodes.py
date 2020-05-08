import os.path
import warnings
import ast

from collections import OrderedDict


nodes = {
    # mod
    ast.Module: ["body"],
    ast.Interactive: ["body"],
    ast.Expression: ["body"],
    ast.Suite: ["body"],
    # stmt
    ast.FunctionDef: ["name", "args", "body", "decorator_list", "returns"],
    ast.AsyncFunctionDef: ["name", "args", "body", "decorator_list", "returns"],
    ast.ClassDef: ["name", "bases", "keywords", "body", "decorator_list"],
    ast.Return: ["value"],
    ast.Delete: ["targets"],
    ast.Assign: ["targets", "value"],
    ast.AugAssign: ["target", "op", "value"],
    ast.AnnAssign: ["target", "annotation", "value", "simple"],
    ast.For: ["target", "iter", "body", "orelse"],
    ast.AsyncFor: ["target", "iter", "body", "orelse"],
    ast.While: ["test", "body", "orelse"],
    ast.If: ["test", "body", "orelse"],
    ast.With: ["items", "body"],
    ast.AsyncWith: ["items", "body"],
    ast.Raise: ["exc", "cause"],
    ast.Try: ["body", "handlers", "orelse", "finalbody"],
    ast.Assert: ["test", "msg"],
    ast.Import: ["names"],
    ast.ImportFrom: ["module", "names", "level"],
    ast.Global: ["names"],
    ast.Nonlocal: ["names"],
    ast.Expr: ["value"],
    ast.Pass: [],
    ast.Break: [],
    ast.Continue: [],
    # expr
    ast.BoolOp: ["op", "values"],
    ast.BinOp: ["left", "op", "right"],
    ast.UnaryOp: ["op", "operand"],
    ast.Lambda: ["args", "body"],
    ast.IfExp: ["test", "body", "orelse"],
    ast.Dict: ["keys", "values"],
    ast.Set: ["elts"],
    ast.ListComp: ["elt", "generators"],
    ast.SetComp: ["elt", "generators"],
    ast.DictComp: ["key", "value", "generators"],
    ast.GeneratorExp: ["elt", "generators"],
    ast.Await: ["value"],
    ast.Yield: ["value"],
    ast.YieldFrom: ["value"],
    ast.Compare: ["left", "ops", "comparators"],
    ast.Call: ["func", "args", "keywords"],
    ast.Num: ["n"],
    ast.Str: ["s"],
    ast.FormattedValue: ["value", "conversion", "format_spec"],
    ast.JoinedStr: ["values"],
    ast.Bytes: ["s"],
    ast.NameConstant: ["value"],
    ast.Ellipsis: [],
    ast.Constant: ["value"],
    ast.Attribute: ["value", "attr"],
    ast.Subscript: ["value", "slice"],
    ast.Starred: ["value"],
    ast.Name: ["id"],
    ast.List: ["elts"],
    ast.Tuple: ["elts"],
    # expr_context
    ast.Load: [],
    ast.Store: [],
    ast.Del: [],
    ast.AugLoad: [],
    ast.AugStore: [],
    ast.Param: [],
    # slice
    ast.Slice: ["lower", "upper", "step"],
    ast.ExtSlice: ["dims"],
    ast.Index: ["value"],
    # boolop
    ast.And: [],
    ast.Or: [],
    # operator
    ast.Sub: [],
    ast.Mult: [],
    ast.MatMult: [],
    ast.Div: [],
    ast.Mod: [],
    ast.Pow: [],
    ast.LShift: [],
    ast.RShift: [],
    ast.BitOr: [],
    ast.BitXor: [],
    ast.BitAnd: [],
    ast.FloorDiv: [],
    # unaryop
    ast.Invert: [],
    ast.Not: [],
    ast.UAdd: [],
    ast.USub: [],
    # cmpop
    ast.Eq: [],
    ast.NotEq: [],
    ast.Lt: [],
    ast.LtE: [],
    ast.Gt: [],
    ast.GtE: [],
    ast.Is: [],
    ast.IsNot: [],
    ast.In: [],
    ast.NotIn: [],
    # comprehension
    ast.comprehension: ["target", "iter", "ifs", "is_async"],
    # excepthandler
    ast.ExceptHandler: ["type", "name", "body"],
    # arguments
    ast.arguments: [
        "args",
        "vararg",
        "kwonlyargs",
        "kw_defaults",
        "kwarg",
        "defaults",
    ],
    # arg
    ast.arg: ["arg", "annotation"],
    # keyword
    ast.keyword: ["arg", "value"],
    # alias
    ast.alias: ["name", "asname"],
    # withitem
    ast.withitem: ["context_expr", "optional_vars"],
}


def convert_node(node):
    t = type(node)

    if t is str or t is int:
        return node

    if t is list:
        return [convert_node(child) for child in node]

    if node is None:
        return "nil"

    tname = t.__qualname__
    d = {"type": tname}

    if t not in nodes:
        return f"#<{tname}>"

    for name in nodes[t]:
        d[name] = convert_node(getattr(node, name))
    return d


def flatten(d, sep="_"):

    obj = OrderedDict()

    def recurse(t, parent_key=""):

        if isinstance(t, list):
            for i in range(len(t)):
                recurse(t[i], parent_key + sep + str(i) if parent_key else str(i))
        elif isinstance(t, dict):
            for k, v in t.items():
                if k == "n" or k == "s":
                    k = "value"
                if v == "Str" or v == "NameConstant" or v == "Num":
                    v = "Constant"
                recurse(v, parent_key + sep + k if parent_key else k)
        else:
            obj[parent_key] = t

    recurse(d)

    return obj