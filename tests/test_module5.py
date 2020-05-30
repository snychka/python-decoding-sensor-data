import pytest
from tests.template import debug_test_case, debug_test_case_class


@pytest.mark.test_energy_create_class_module5
def test_energy_create_class_module5(parse):
    # from house_info import HouseInfo
    # class EnergyData(HouseInfo):
    #       ENERGY_PER_BULB = 0.2        # in watts
    #       ENERGY_BITS = 0x0F0

    test_file = "energy_info"
    parent_class = "HouseInfo"
    test_class = "EnergyData"
    test_method = "_convert_data"

    my_file = parse(test_file)
    assert my_file.success, my_file.message

    my_file_import = my_file.from_imports(
        "house_info", "HouseInfo")
    
    assert my_file_import, "Are you importing `HouseInfo` from `house_info` in `{}` file".format(test_file)
    my_class = my_file.query("class {0}({1}): ??".format(test_class, parent_class))
    assert (
        my_class.exists()
    ), """Have you created a class called `{0}`?
        Is your class inheriting the properties of the `{1}` class?""".format(test_class, parent_class)

    # debug_test_case_class(my_class, test_method) 

    
    test_code = (
        my_class.assign_().match(
            {
                "0_type": "Assign",
                "0_targets_0_type": "Name",
                "0_targets_0_id": "ENERGY_PER_BULB",
                "0_value_type": "Constant",
                "0_value_value": "#<float>",

                "1_type": "Assign",
                "1_targets_0_type": "Name",
                "1_targets_0_id": "ENERGY_BITS",
                "1_value_type": "Constant",
                "1_value_value": 240
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Are you declararing a constant `ENERGY_PER_BULB`?
        Did you set it to `0.2` float number?
        Are you declararing a constant `ENERGY_BITS`?
        Did you set it to `0x0F0` hex number?"""
   
  
@pytest.mark.test_energy_get_energy_method_module5
def test_energy_get_energy_method_module5(parse):
    # def _get_energy(self, rec):
    #     energy = int(rec, base=16)
    #     energy = energy & self.ENERGY_BITS            # mask ENERGY bits
    #     energy = energy >> 4                          # shift right
    #     return energy

    test_file = "energy_info"
    parent_class = "HouseInfo"
    test_class = "EnergyData"
    test_method = "_get_energy"

    my_file = parse(test_file)
    assert my_file.success, my_file.message

    my_class = my_file.query("class {0}({1}): ??".format(test_class, parent_class))
    assert (
        my_class.exists()
    ), """Have you created a class called `{0}`?
        Is your class inheritings the properties of the `{1}` class?""".format(test_class, parent_class)
    
    # debug_test_case_class(my_class, test_method) 

    my_method = my_file.class_(test_class).method(test_method)
    assert (
        my_method.exists()
    ), "Are you defining a method called `{}`?".format(test_method)
    
    # debug_test_case(my_method) 
    
    my_class_arguments = (
        my_class.def_args_(test_method).match(
            {
                "type": "FunctionDef",
                "name": "_get_energy",
                "args_type": "arguments",
                "args_args_0_type": "arg",
                "args_args_0_arg": "self",
                "args_args_0_annotation": "nil",
                "args_args_1_type": "arg",
                "args_args_1_arg": "rec",
                "args_args_1_annotation": "nil",
                "args_vararg": "nil",
                "args_kwarg": "nil",
            }
        )
        .exists()
    )
    assert (
        my_class_arguments
    ), """Are you defining a method `{0}` for the `{1}` class?
        Are you declaring the correct name and number of parameters?""".format(test_method, test_class)
    
    # Check for assignment 
    test_code = (
        my_method.assign_().match(
            {
                "0_type": "Assign",
                "0_targets_0_type": "Name",
                "0_targets_0_id": "energy",
                "0_value_type": "Call",
                "0_value_func_type": "Name",
                "0_value_func_id": "int",
                "0_value_args_0_type": "Name",
                "0_value_args_0_id": "rec",
                "0_value_keywords_0_type": "keyword",
                "0_value_keywords_0_arg": "base",
                "0_value_keywords_0_value_type": "Constant",
                "0_value_keywords_0_value_value": 16,
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Are you converting `rec` as an `int()` with `base=16`?
        Are you assigning the result to a variable called `energy`?"""

    test_code = (
        my_method.assign_().match(
            {
                "1_type": "Assign",
                "1_targets_0_type": "Name",
                "1_targets_0_id": "energy",
                "1_value_type": "BinOp",
                "1_value_left_type": "Name",
                "1_value_left_id": "energy",
                "1_value_op_type": "BitAnd",
                "1_value_right_type": "Attribute",
                "1_value_right_value_type": "Name",
                "1_value_right_value_id": "self",
                "1_value_right_attr": "ENERGY_BITS",
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Are you converting `energy` by "anding it" with `self.ENERGY_BITS`?"""
    
    test_code = (
        my_method.assign_().match(
            {
                "2_type": "Assign",
                "2_targets_0_type": "Name",
                "2_targets_0_id": "energy",
                "2_value_type": "BinOp",
                "2_value_left_type": "Name",
                "2_value_left_id": "energy",
                "2_value_op_type": "RShift",
                "2_value_right_type": "Constant",
                "2_value_right_value": 4
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Are you converting `energy` by shifting the bits to the right 4 positions?"""
    
    test_code = (
        my_method.returns_call().match(
            {
                "type": "Return",
                "value_type": "Name",
                "value_id": "energy"
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Are you returning `energy` from the `{}` method?""".format(test_method)


@pytest.mark.test_energy_convert_method_module5
def test_energy_convert_method_module5(parse):
    #    def _convert_data(self, data):
    #         recs = []
    #         for rec in data:
    #               # Convert string of integers into actual integers based 16
    #               recs.append(self._get_energy(rec))
    #          return recs
    test_file = "energy_info"
    parent_class = "HouseInfo"
    test_class = "EnergyData"
    test_method = "_convert_data"

    my_file = parse(test_file)
    assert my_file.success, my_file.message

    my_file_import = my_file.from_imports(
        "house_info", "HouseInfo")
    
    assert my_file_import, "Are you importing `HouseInfo` from `house_info` in `{}` file".format(test_file)
    my_class = my_file.query("class {0}({1}): ??".format(test_class, parent_class))
    assert (
        my_class.exists()
    ), """Have you created a class called `{0}`?
        Is your class inheritings the properties of the `{1}` class?""".format(test_class, parent_class)

    # debug_test_case_class(my_class, test_method) 

    my_method = my_file.class_(test_class).method(test_method)
    assert (
        my_method.exists()
    ), "Are you defining a method called `{}`?".format(test_method)
    
    # debug_test_case(my_method) 
    
    my_class_arguments = (
        my_class.def_args_(test_method).match(
            {
                "type": "FunctionDef",
                "name": "_convert_data",
                "args_type": "arguments",
                "args_args_0_type": "arg",
                "args_args_0_arg": "self",
                "args_args_0_annotation": "nil",
                "args_args_1_type": "arg",
                "args_args_1_arg": "data",
                "args_args_1_annotation": "nil",
                "args_vararg": "nil",
                "args_kwarg": "nil",
            }
        )
        .exists()
    )
    assert (
        my_class_arguments
    ), """Are you defining a method `{0}` for the `{1}` class?
        Are you declaring the correct name and number of parameters?""".format(test_method, test_class)
    
    # Check for assignment 
    test_code = (
        my_method.assign_().match(
            {
                "targets_0_type": "Name",
                "targets_0_id": "recs",
                "value_type": "List"
            }
        )
        .exists()
    )
    assert (
        test_code
    ), "Are you creating a variable called `recs` set equal to an empty list?"
    
    test_code = (
        my_method.for_().match(
            {
                "target_type": "Name",
                "target_id": "rec",
                "iter_type": "Name",
                "iter_id": "data"
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Do you have a `for` loop, looping through `data`? 
        Is the current loop value called `rec`?"""

    test_code = (
        my_method.for_().match(
            {
                "0_type": "Expr",
                "0_value_type": "Call",
                "0_value_func_type": "Attribute",
                "0_value_func_value_type": "Name",
                "0_value_func_value_id": "recs",
                "0_value_func_attr": "append",
                "0_value_args_0_type": "Call",
                "0_value_args_0_func_type": "Attribute",
                "0_value_args_0_func_value_type": "Name",
                "0_value_args_0_func_value_id": "self",
                "0_value_args_0_func_attr": "_get_energy",
                "0_value_args_0_args_0_type": "Name",
                "0_value_args_0_args_0_id": "rec"
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Inside your loop, are you converting `rec` value through `self._rec_energy()` method?
        Are you appending it to `recs` list?"""
    
    test_code= (
        my_method.returns_call().match(
            {
                "type": "Return",
                "value_type": "Name",
                "value_id": "recs"
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Are you returning `recs` list from the `{}` method?""".format(test_method)


@pytest.mark.test_energy_by_area_and_date_methods_module5
def test_energy_by_area_and_date_methods_module5(parse):
    # from datetime import date
    # def get_data_by_area(self, rec_area=0):
    #     data = super().get_data_by_area("energy_usage", rec_area)
    #     return self._convert_data(recs)
    #
    # def get_data_by_date(self, rec_date=date.today()):
    #     recs = super().get_data_by_date("energy_usage", rec_date)
    #     return self._convert_data(recs)
    
    test_file = "energy_info"
    parent_class = "HouseInfo"
    test_class = "EnergyData"
    test_method = "get_data_by_area"
    
    my_file = parse(test_file)
    assert my_file.success, my_file.message

    my_class = my_file.query("class {0}({1}): ??".format(test_class, parent_class))
    assert (
        my_class.exists()
    ), """Have you created a class called `{0}`?
        Is your class inheritings the properties of the `{1}` class?""".format(test_class, parent_class)

    # debug_test_case_class(my_class, test_method) 
    
    my_method = my_file.class_(test_class).method(test_method)
    assert (
        my_method.exists()
    ), "Are you defining a method called `{}`?".format(test_method)
    
    # debug_test_case(my_method) 

    my_class_arguments = (
        my_class.def_args_(test_method).match(
            {
                "type": "FunctionDef",
                "name": "get_data_by_area",
                "args_type": "arguments",
                "args_args_0_type": "arg",
                "args_args_0_arg": "self",
                "args_args_0_annotation": "nil",
                "args_args_1_type": "arg",
                "args_args_1_arg": "rec_area",
                "args_args_1_annotation": "nil",
                "args_vararg": "nil",
                "args_kwarg": "nil",
                "args_defaults_0_type": "Constant",
                "args_defaults_0_value": 0,
            }
        )
        .exists()
    )
    assert (
        my_class_arguments
    ), """Are you defining a method `{0}` for the `{1}` class?
        Are you declaring the correct name and number of parameters?""".format(test_method, test_class)

    test_code = (
        my_method.assign_().match(
            {
                "type": "Assign",
                "targets_0_type": "Name",
                "targets_0_id": "recs",
                "value_type": "Call",
                "value_func_type": "Attribute",
                "value_func_value_type": "Call",
                "value_func_value_func_type": "Name",
                "value_func_value_func_id": "super",
                "value_func_attr": "get_data_by_area",
                "value_args_0_type": "Constant",
                "value_args_0_value": "energy_usage",
                "value_args_1_type": "Name",
                "value_args_1_id": "rec_area"
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Are you creating a variable called `recs` set equal to 
        the `{}` method from the `{}` parent class?
        Are you passing "energy" as the only argument to the method call?""".format(test_method, parent_class)

    test_code = (
        my_method.returns_call().match(
            {
                "type": "Return",
                "value_type": "Call",
                "value_func_type": "Attribute",
                "value_func_value_type": "Name",
                "value_func_value_id": "self",
                "value_func_attr": "_convert_data",
                "value_args_0_type": "Name",
                "value_args_0_id": "recs"
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Are you returning a call from the `{}` method?
        Are you calling the `_convert_data` method?
        Passing `recs` as the only argument?""".format(test_method)

    # Now test get_data_by_date
    test_method = "get_data_by_date"
    
    my_file_import = my_file.from_imports(
        "datetime", "date")
    assert my_file_import, "Are you importing `date` from datetime in `{}`".format(test_file)
    
    my_method = my_file.class_(test_class).method(test_method)
    assert (
        my_method.exists()
    ), "Are you defining a method called `{}`?".format(test_method)
    
    # debug_test_case(my_method) 

    my_class_arguments = (
        my_class.def_args_(test_method).match(
            {
                "type": "FunctionDef",
                "name": "get_data_by_date",
                "args_type": "arguments",
                "args_args_0_type": "arg",
                "args_args_0_arg": "self",
                "args_args_0_annotation": "nil",
                "args_args_1_type": "arg",
                "args_args_1_arg": "rec_date",
                "args_args_1_annotation": "nil",
                "args_vararg": "nil",
                "args_kwarg": "nil",
                "args_defaults_0_type": "Call",
                "args_defaults_0_func_type": "Attribute",
                "args_defaults_0_func_value_type": "Name",
                "args_defaults_0_func_value_id": "date",
                "args_defaults_0_func_attr": "today",
            }
        )
        .exists()
    )
    assert (
        my_class_arguments
    ), """Are you defining a method `{0}` for the `{1}` class?
        Are you declaring the correct name and number of parameters?""".format(test_method, test_class)

    test_code = (
        my_method.assign_().match(
            {
                "type": "Assign",
                "targets_0_type": "Name",
                "targets_0_id": "recs",
                "value_type": "Call",
                "value_func_type": "Attribute",
                "value_func_value_type": "Call",
                "value_func_value_func_type": "Name",
                "value_func_value_func_id": "super",
                "value_func_attr": "get_data_by_date",
                "value_args_0_type": "Constant",
                "value_args_0_value": "energy_usage",
                "value_args_1_type": "Name",
                "value_args_1_id": "rec_date"
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Are you creating a variable called `recs` set equal to 
        the `{}` method from the `{}` parent class?
        Are you passing "energy" as the only argument to the method call?""".format(test_method, parent_class)

    # debug_test_case(my_method) 

    test_code = (
        my_method.returns_call().match(
            {
                "type": "Return",
                "value_type": "Call",
                "value_func_type": "Attribute",
                "value_func_value_type": "Name",
                "value_func_value_id": "self",
                "value_func_attr": "_convert_data",
                "value_args_0_type": "Name",
                "value_args_0_id": "recs"
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Are you returning a call from the `{}` method?
        Are you calling the `_convert_data` method?
        Passing `recs` as the only argument?""".format(test_method)


@pytest.mark.test_energy_calculate_usage_method_module5
def test_energy_calculate_usage_method_module5(parse):
    #      def calculate_energy_usage(self, data):
    #         total_energy = sum([field * self.ENERGY_PER_BULB for field in data])
    #         return total_energy
    
    test_file = "energy_info"
    parent_class = "HouseInfo"
    test_class = "EnergyData"
    test_method = "calculate_energy_usage"
    
    my_file = parse(test_file)
    assert my_file.success, my_file.message

    my_file_import = my_file.from_imports(
        "datetime", "date")
    assert my_file_import, "Are you importing `date` from datetime in `{}`".format(test_file)
    
    my_class = my_file.query("class {0}({1}): ??".format(test_class, parent_class))
    assert (
        my_class.exists()
    ), """Have you created a class called `{0}`?
        Is your class inheritings the properties of the `{1}` class?""".format(test_class, parent_class)

    # debug_test_case_class(my_class, test_method) 
    
    my_method = my_file.class_(test_class).method(test_method)
    assert (
        my_method.exists()
    ), "Are you defining a method called `{}`?".format(test_method)
    
    # debug_test_case(my_method) 

    my_class_arguments = (
        my_class.def_args_(test_method).match(
            {
                "type": "FunctionDef",
                "name": "calculate_energy_usage",
                "args_type": "arguments",
                "args_args_0_type": "arg",
                "args_args_0_arg": "self",
                "args_args_0_annotation": "nil",
                "args_args_1_type": "arg",
                "args_args_1_arg": "data",
                "args_args_1_annotation": "nil",
                "args_vararg": "nil",
                "args_kwarg": "nil",
            }
        )
        .exists()
    )
    assert (
        my_class_arguments
    ), """Are you defining a method `{0}` for the `{1}` class?
        Are you declaring the correct name and number of parameters?""".format(test_method, test_class)

    test_code = (
        my_method.assign_().match(
            {
                "type": "Assign",
                "targets_0_type": "Name",
                "targets_0_id": "total_energy",
                "value_type": "Call",
                "value_func_type": "Name",
                "value_func_id": "sum",
                "value_args_0_type": "ListComp",
                "value_args_0_elt_type": "BinOp",
                "value_args_0_elt_left_type": "Name",
                "value_args_0_elt_left_id": "field",
                "value_args_0_elt_op_type": "Mult",
                "value_args_0_elt_right_type": "Attribute",
                "value_args_0_elt_right_value_type": "Name",
                "value_args_0_elt_right_value_id": "self",
                "value_args_0_elt_right_attr": "ENERGY_PER_BULB",
                "value_args_0_generators_0_type": "comprehension",
                "value_args_0_generators_0_target_type": "Name",
                "value_args_0_generators_0_target_id": "field",
                "value_args_0_generators_0_iter_type": "Name",
                "value_args_0_generators_0_iter_id": "data",
                "value_args_0_generators_0_is_async": 0
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Are you declaring a variable called `total_energy`?
        Are you setting it to `sum()` built it function?
        Are you passing a `list comprehension` as an argument to `sum()`?
        Are you setting `field * self.ENERGY_PER_BULB` as you `list comprehension` expression?
        Are you iterating over `data` in your `list comprehension`?
        """
    
    test_code = (
        my_method.returns_call().match(
            {
                "type": "Return",
                "value_type": "Name",
                "value_id": "total_energy"
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Are you returning a `total_energy` from the `{}` method?""".format(test_method)


@pytest.mark.test_sensor_app_energy_info_by_area_module5
def test_sensor_app_energy_info_by_area_module5(parse):
    # from energy_info import EnergyData          # module 4
    # ...
    # energy_data = EnergyData(data)
    # recs = energy_data.get_data_by_area(rec_area=test_area)
    # print("\nHouse Energy sensor records for area {} = {}".format(test_area, len(recs)))
    # total_energy = energy_data.calculate_energy_usage(data=recs)
    # print("\tEnergy Usage: {:2.2} Watts".format(total_energy))

    test_file = "sensor_app"
    test_class = "EnergyData"
    
    my_file = parse(test_file)
    assert my_file.success, my_file.message

    my_file_import = my_file.from_imports(
        "energy_info", "EnergyData")
    assert my_file_import, "Are you importing `EnergyData` from `energy_info` in `{}`".format(test_file)

    # debug_test_case(my_file)    

    test_code = (
        my_file.assign_().match(
            {
                "18_type": "Assign",
                "18_targets_0_type": "Name",
                "18_targets_0_id": "energy_data",
                "18_value_type": "Call",
                "18_value_func_type": "Name",
                "18_value_func_id": "EnergyData",
                "18_value_args_0_type": "Name",
                "18_value_args_0_id": "data",
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Are you creating an instance of the '{}' class called `energy_data`
        Are you passing `data` as the initialization argument for the constructor?
        """.format(test_class)
    
    test_code = (
        my_file.assign_().match(
            {
                "19_type": "Assign",
                "19_targets_0_type": "Name",
                "19_targets_0_id": "recs",
                "19_value_type": "Call",
                "19_value_func_type": "Attribute",
                "19_value_func_value_type": "Name",
                "19_value_func_value_id": "energy_data",
                "19_value_func_attr": "get_data_by_area",
                "19_value_keywords_0_type": "keyword",
                "19_value_keywords_0_arg": "rec_area",
                "19_value_keywords_0_value_type": "Name",
                "19_value_keywords_0_value_id": "test_area",
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Are you setting `recs` to the method call `get_data_by_area` from the `energy_data` object?
        Are you passing `rec_area=test_area` as the only argument to the method?
        """
    
    test_code = (
        my_file.assign_().match(
            {
                "20_type": "Assign",
                "20_targets_0_type": "Name",
                "20_targets_0_id": "total_energy",
                "20_value_type": "Call",
                "20_value_func_type": "Attribute",
                "20_value_func_value_type": "Name",
                "20_value_func_value_id": "energy_data",
                "20_value_func_attr": "calculate_energy_usage",
                "20_value_keywords_0_type": "keyword",
                "20_value_keywords_0_arg": "data",
                "20_value_keywords_0_value_type": "Name",
                "20_value_keywords_0_value_id": "recs",
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Are you setting `total_energy` to the method call `calculate_energy_usage` from the `energy_data` object?
        Are you passing `data=recs` as the only argument to the method?
        """


@pytest.mark.test_sensor_app_energy_info_by_date_module5
def test_sensor_app_energy_info_by_date_module5(parse):
    # ...
    # recs = energy_data.get_data_by_date(rec_date=test_date)
    # print("House Energy sensor records for date: {} = {}".format(
    #     test_date.strftime("%m/%d/%y"), len(recs)))
    # total_energy = energy_data.calculate_energy_usage(data=recs)
    # print("\tEnergy Usage: {:2.2} Watts".format(total_energy))

    test_file = "sensor_app"
    test_class = "EnergyData"
    
    my_file = parse(test_file)
    assert my_file.success, my_file.message

    # debug_test_case(my_file)   

    test_code = (
        my_file.assign_().match(
            {
                "21_type": "Assign",
                "21_targets_0_type": "Name",
                "21_targets_0_id": "recs",
                "21_value_type": "Call",
                "21_value_func_type": "Attribute",
                "21_value_func_value_type": "Name",
                "21_value_func_value_id": "energy_data",
                "21_value_func_attr": "get_data_by_date",
                "21_value_keywords_0_type": "keyword",
                "21_value_keywords_0_arg": "rec_date",
                "21_value_keywords_0_value_type": "Name",
                "21_value_keywords_0_value_id": "test_date",
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Are you setting `recs` to the method call `get_data_by_date` from the `energy_data` object?
        Are you passing `rec_date=test_date` as the only argument to the method?
        """

    test_code = (
        my_file.assign_().match(
            {
                "22_type": "Assign",
                "22_targets_0_type": "Name",
                "22_targets_0_id": "total_energy",
                "22_value_type": "Call",
                "22_value_func_type": "Attribute",
                "22_value_func_value_type": "Name",
                "22_value_func_value_id": "energy_data",
                "22_value_func_attr": "calculate_energy_usage",
                "22_value_keywords_0_type": "keyword",
                "22_value_keywords_0_arg": "data",
                "22_value_keywords_0_value_type": "Name",
                "22_value_keywords_0_value_id": "recs"
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Are you setting `total_energy` to the method call `calculate_energy` from the `energy_data` object?
        Are you passing `data=recs` as the only argument to the method?
        """
