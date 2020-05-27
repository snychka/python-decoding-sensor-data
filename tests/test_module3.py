import pytest
from tests.template import debug_test_case, debug_test_case_class


@pytest.mark.test_temperature_import_module3
def test_temperature_import_module3(parse):
    # from house_info import HouseInfo

    test_file = "temperature_info"
    
    my_file = parse(test_file)
    assert my_file.success, my_file.message

    my_file_import = my_file.from_imports(
        "house_info", "HouseInfo")
    assert my_file_import, "Are you importing `HouseInfo` from `house_info` in `{}` file".format(test_file)


@pytest.mark.test_temperature_create_class_module3
def test_temperature_create_class_module3(parse):
    # class TemperatureData(HouseInfo):
    #    def _convert_data(self, data):
    #         data = []

    test_file = "temperature_info"
    parent_class = "HouseInfo"
    test_class = "TemperatureData"
    test_method = "_convert_data"

    my_file = parse(test_file)
    assert my_file.success, my_file.message

    my_class = my_file.query("class {0}({1}): ??".format(test_class, parent_class))
    assert (
        my_class.exists()
    ), """Have you created a class called `{0}`?
        Is your class inheritings the properties of the `{1}` class?""".format(test_class, parent_class)

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
    

@pytest.mark.test_temperature_convert_loop_module3
def test_temperature_convert_loop_module3(parse):
    # for rec in data:
    #     # Convert string of integers into actual integers based 10
    #     recs.append(int(rec, base=10))
    # return recs

    test_file = "temperature_info"
    parent_class = "HouseInfo"
    test_class = "TemperatureData"
    test_method = "_convert_data"
   
    my_file = parse(test_file)
    assert my_file.success, my_file.message

    my_class = my_file.query("class {0}({1}): ??".format(test_class, parent_class))
    assert (
        my_class.exists()
    ), """Have you created a class called `{0}`?
        Is your class inheritings the properties of the `{1}` class?""".format(test_class, parent_class)

    my_method = my_file.class_(test_class).method(test_method)
    assert (
        my_method.exists()
    ), "Are you defining a method called `{}`?".format(test_method)
    
    # debug_test_case(my_method) 

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
                "0_value_args_0_func_type": "Name",
                "0_value_args_0_func_id": "int",
                "0_value_args_0_args_0_type": "Name",
                "0_value_args_0_args_0_id": "rec",
                "0_value_args_0_keywords_0_type": "keyword",
                "0_value_args_0_keywords_0_arg": "base",
                "0_value_args_0_keywords_0_value_type": "Constant",
                "0_value_args_0_keywords_0_value_value": 10
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Inside your loop, are you converting `rec` value to integer `base=10`
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


@pytest.mark.test_temperature_by_area_method_module3
def test_temperature_by_area_method_module3(parse):
    # def get_data_by_area(self, rec_area=0):
    #     data = super().get_data_by_area("temperature", rec_area)
    
    test_file = "temperature_info"
    parent_class = "HouseInfo"
    test_class = "TemperatureData"
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
                "value_args_0_value": "temperature",
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
        Are you passing `"temperature"` as the first argument to the method call?
        Are you passing `rec_area` as the second argument to the method call?""".format(test_method, parent_class)

@pytest.mark.test_temperature_by_area_method_return_module3
def test_temperature_by_area_method_return_module3(parse):
    # ...
    #     return self._convert_data(recs)
    
    test_file = "temperature_info"
    parent_class = "HouseInfo"
    test_class = "TemperatureData"
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

@pytest.mark.test_temperature_by_date_method_module3
def test_temperature_by_date_method_module3(parse):
    # from datetime import date
    # def get_data_by_date(self, rec_date=date.today()):
    #     recs = super().get_data_by_date("temperature", rec_date)
    
    test_file = "temperature_info"
    parent_class = "HouseInfo"
    test_class = "TemperatureData"
    test_method = "get_data_by_date"
    
    my_file = parse(test_file)
    assert my_file.success, my_file.message

    my_file_import = my_file.from_imports(
        "datetime", "date")
    assert my_file_import, "Are you importing `date` from `datetime` in `{}`".format(test_file)
    
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
                "value_args_0_value": "temperature",
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
        Are you passing `"temperature"` as the first argument to the method call?
        Are you passing `rec_date` as the second argument to the method call?""".format(test_method, parent_class)


@pytest.mark.test_temperature_by_date_method_return_module3
def test_temperature_by_date_method_return_module3(parse):
    # ...
    #     return self._convert_data(recs)
    
    test_file = "temperature_info"
    parent_class = "HouseInfo"
    test_class = "TemperatureData"
    test_method = "get_data_by_date"
    
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


@pytest.mark.test_sensor_app_temp_info_by_area_module3
def test_sensor_app_temp_info_by_area_module3(parse):
    # from temperature_info import TemperatureData
    # ...
    # temperature_data = TemperatureData(data)
    # recs = temperature_data.get_data_by_area(rec_area=test_area)
    # print("\nHouse Temperature sensor records for area {} = {}".format(test_area, len(recs)))
    # print("\tMaximum: {0}, Minimum: {1}, and Averrage: {2} temperatures".format( max(recs), min(recs)))

    test_file = "sensor_app"
    test_class = "TemperatureData"
    
    my_file = parse(test_file)
    assert my_file.success, my_file.message

    my_file_import = my_file.from_imports(
        "temperature_info", "TemperatureData")
    assert my_file_import, "Are you importing `{0}` from `temperature_info` in `{}`".format(test_file)


    # debug_test_case(my_file)    

    test_code = (
        my_file.assign_().match(
            {
                "7_type": "Assign",
                "7_targets_0_type": "Name",
                "7_targets_0_id": "temperature_data",
                "7_value_type": "Call",
                "7_value_func_type": "Name",
                "7_value_func_id": "TemperatureData",
                "7_value_args_0_type": "Name",
                "7_value_args_0_id": "data",
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Are you creating an instance of the '{}' class called `temperature_data`?
        Are you passing `data` list as the initialization argument for the constructor?

        """.format(test_class)
    
    test_code = (
        my_file.assign_().match(
            {
                "8_type": "Assign",
                "8_targets_0_type": "Name",
                "8_targets_0_id": "recs",
                "8_value_type": "Call",
                "8_value_func_type": "Attribute",
                "8_value_func_value_type": "Name",
                "8_value_func_value_id": "temperature_data",
                "8_value_func_attr": "get_data_by_area",
                "8_value_keywords_0_type": "keyword",
                "8_value_keywords_0_arg": "rec_area",
                "8_value_keywords_0_value_type": "Name",
                "8_value_keywords_0_value_id": "test_area",
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Are you setting `recs` to the method call `get_data_by_area` from the `temperature_data` object?
        Are you passing `rec_area=test_area` as the only argument to the method?
        """


@pytest.mark.test_sensor_app_temp_info_by_date_module3
def test_sensor_app_temp_info_by_date_module3(parse):
    # ...
    # recs = temperature_data.get_data_by_date(test_date)
    # NOTE: print statements are not validated
    # print("House Temperature sensor records for date: {} = {}".format(test_date.strftime("%m/%d/%y"), len(recs)))
    # print("\tMaximum: {0}, Minimum: {1}, and Averrage: {2} temperatures".format(max(recs), min(recs), mean(recs)))

    test_file = "sensor_app"
    test_class = "TemperatureData"
    
    my_file = parse(test_file)
    assert my_file.success, my_file.message

    # debug_test_case(my_file)    

    test_code = (
        my_file.assign_().match(
            {
                "9_type": "Assign",
                "9_targets_0_type": "Name",
                "9_targets_0_id": "recs",
                "9_value_type": "Call",
                "9_value_func_type": "Attribute",
                "9_value_func_value_type": "Name",
                "9_value_func_value_id": "temperature_data",
                "9_value_func_attr": "get_data_by_date",
                "9_value_keywords_0_type": "keyword",
                "9_value_keywords_0_arg": "rec_date",
                "9_value_keywords_0_value_type": "Name",
                "9_value_keywords_0_value_id": "test_date",
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Are you setting `recs` to the method call `get_data_by_date` from the `temperature_data` object?
        Are you passing `rec_date=test_date` as the only argument to the method?
        """
