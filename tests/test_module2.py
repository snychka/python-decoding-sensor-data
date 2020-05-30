import pytest
from tests.template import debug_test_case, debug_test_case_class

try:
    from sensor.load_data import load_sensor_data 
    recs = load_sensor_data()
except ImportError:
    recs = 0

try:
    from sensor.house_info import HouseInfo
    home_info = HouseInfo(recs)
except ImportError:
    home_info = 0

from datetime import date, datetime

@pytest.mark.test_house_info_create_class_module2
def test_house_info_create_class_module2(parse):
    # class HouseInfo():
    #     def __init__(self, data):
    #         self.data = data

    test_file = "house_info"
    test_class = "HouseInfo"
    test_method = "__init__"

    my_file = parse(test_file)
    assert my_file.success, my_file.message
    
    # my_class = house_info.class_(test_class)
    my_class = my_file.query("class {}(): ??".format(test_class))
    assert (
        my_class.exists()
    ), "Have you created a class called `{0}` in the `{1}` file?".format(test_class, test_file)

    my_method = my_file.class_(test_class).method(test_method)
    assert (
        my_method.exists()
    ), "Are you defining a constructor called `{}`?".format(test_method)
    
    
    my_class_arguments = (
        my_class.def_args_(test_method).match(
            {
                "type": "FunctionDef",
                "name": "__init__",
                "args_type": "arguments",
                "args_args_0_type": "arg",
                "args_args_0_arg": "self",
                "args_args_0_annotation": "nil",
                "args_args_1_type": "arg",
                "args_args_1_arg": "data",
                "args_args_1_annotation": "nil",
            }
        )
        .exists()
    )
    assert (
        my_class_arguments
    ), """Are you defining a constructor `{0}` for the `{1}` class?
        Are you declaring the correct name and number of parameters?""".format(test_method, test_class)
    
    # debug_test_case(my_method) 
    
    # Check for assignment 
    test_code = (
        my_method.assign_().match(
            {
                "type": "Assign",
                "targets_0_type": "Attribute",
                "targets_0_value_type": "Name",
                "targets_0_value_id": "self",
                "targets_0_attr": "data",
                "value_type": "Name",
                "value_id": "data"
            }
        )
        .exists()
    )
    assert (
        test_code
    ), "Are you creating a class attribute `self.data` and setting it equal to `data`?"
    
    
@pytest.mark.test_house_info_get_data_by_area_module2
def test_house_info_get_data_by_area_module2(parse):
    
    # def get_data_by_area(self, field, rec_area=0):
        # field_data = []
    
    test_file = "house_info"
    test_class = "HouseInfo"
    test_method = "get_data_by_area"

    my_file = parse(test_file)
    assert my_file.success, my_file.message
    
    # my_class = house_info.class_(test_class)
    my_class = my_file.query("class {}(): ??".format(test_class))
    assert (
        my_class.exists()
    ), "Have you created a class called `{0}` in the `{1}` file?".format(test_class, test_file)

    my_method = my_file.class_(test_class).method(test_method)
    assert (
        my_method.exists()
    ), "Are you defining a method called `{}`?".format(test_method)
    
    # debug_test_case(my_method) 

    my_class_arguments = (
        my_class.def_args_(test_method).match(
            {
                "type": "FunctionDef",
                "name": test_method,
                "args_type": "arguments",
                "args_args_0_type": "arg",
                "args_args_0_arg": "self",
                "args_args_0_annotation": "nil",
                "args_args_1_type": "arg",
                "args_args_1_arg": "field",
                "args_args_1_annotation": "nil",
                "args_args_2_type": "arg",
                "args_args_2_arg": "rec_area",
                "args_args_2_annotation": "nil",
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
                "targets_0_id": "field_data",
                "value_type": "List"
            }
        )
        .exists()
    )
    assert (
        test_code
    ), "Are you creating a variable called `field_data` set equal to an empty list?"


@pytest.mark.test_house_info_get_data_by_area_loop_module2
def test_house_info_get_data_by_area_loop_module2(parse):
    
    #     for record in self.data:
            # if rec_area == 0:
            #     field_data.append(record[field])
            # elif rec_area == int(record['area']): 
            #     field_data.append(record[field])
    #     return field_data

    test_file = "house_info"
    test_class = "HouseInfo"
    test_method = "get_data_by_area"

    my_file = parse(test_file)
    assert my_file.success, my_file.message
    
    # my_class = house_info.class_(test_class)
    my_class = my_file.query("class {}(): ??".format(test_class))
    assert (
        my_class.exists()
    ), "Have you created a class called `{0}` in the `{1}` file?".format(test_class, test_file)

    my_method = my_file.class_(test_class).method(test_method)
    assert (
        my_method.exists()
    ), "Are you defining a method called `{}`?".format(test_method)
    
    # debug_test_case(my_method) 

    test_code = (
        my_method.for_().match(
            {

                "target_type": "Name",
                "target_id": "record",
                "iter_type": "Attribute",
                "iter_value_type": "Name",
                "iter_value_id": "self",
                "iter_attr": "data"
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Do you have a `for` loop, looping through `self.data`? 
        Is the current loop value called `record`?"""


    # Test filer options:
    # recs = sensor.load_data.load_sensor_data()    # defined at top of file
    home_info = HouseInfo(recs)
    home_temp = home_info.get_data_by_area("id")
    assert (
        len(home_temp) == 2000
    ), """The length of your filter data when calling `get_data_by_area` is incorrect.
        Your function call should have only one argument. For example: `id`
        Check the logic inside your loop"""

    home_temp = home_info.get_data_by_area("id", rec_area=1)
    assert (
        len(home_temp) == 1000
    ), """The length of your filter data when calling `get_data_by_area` is incorrect.
        Your call should have the first argument as `id`, and the second argument as `rec_area=1
        Check the logic inside your loop"""

    home_temp = home_info.get_data_by_area("id", rec_area=2)
    assert (
        len(home_temp) == 1000
    ), """The length of your filter data when calling `get_data_by_area` is incorrect.
        Your call should have the first argument as `id`, and the second argument as `rec_area=2
        Check the logic inside your loop"""
    
    home_temp = home_info.get_data_by_area("id", rec_area=-999)
    assert (
        len(home_temp) == 0
    ), """The length of your filter data when calling `get_data_by_area` is incorrect.
        Your call should have the first argument as `id`, and the second argument as `rec_area=-999
        Check the logic inside your loop"""


@pytest.mark.test_house_info_get_data_by_date_module2
def test_house_info_get_data_by_date_module2(parse):

    # from datetime import date, datetime
    # def get_data_by_date(self, field, rec_date=date.today()):
    #     field_data = []

    test_file = "house_info"
    test_class = "HouseInfo"
    test_method = "get_data_by_date"

    my_file = parse(test_file)
    assert my_file.success, my_file.message
    
    # my_class = house_info.class_(test_class)
    my_class = my_file.query("class {}(): ??".format(test_class))
    assert (
        my_class.exists()
    ), "Have you created a class called `{0}` in the `{1}` file?".format(test_class, test_file)

    my_method = my_file.class_(test_class).method(test_method)
    assert (
        my_method.exists()
    ), "Are you defining a method called `{}`?".format(test_method)
    
    # debug_test_case(my_method) 

    house_info_import = my_file.from_imports(
        "datetime", "date")
    assert house_info_import, "Are you importing `date` from `datetime`?"


    my_class_arguments = (
        my_class.def_args_(test_method).match(
            {
                "type": "FunctionDef",
                "name": test_method,
                "args_type": "arguments",
                "args_args_0_type": "arg",
                "args_args_0_arg": "self",
                "args_args_0_annotation": "nil",
                "args_args_1_type": "arg",
                "args_args_1_arg": "field",
                "args_args_1_annotation": "nil",
                "args_args_2_type": "arg",
                "args_args_2_arg": "rec_date",
                "args_args_2_annotation": "nil",
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
    ), """Are you defining a method `get_data_by_date` 
        with the correct name and number of parameters?
        Are you setting the third parameter's default value to `date.today()`?"""
    
    # debug_test_case(my_method) 

    test_code = (
        my_method.assign_().match(
            {
                "type": "Assign",
                "targets_0_type": "Name",
                "targets_0_id": "field_data",
                "value_type": "List"
            }
        )
        .exists()
    )
    assert (
        test_code
    ), "Are you creating a variable called `field_data` set equal to an empty list?"
    
    
@pytest.mark.test_house_info_get_data_by_date_loop_module2
def test_house_info_get_data_by_date_loop_module2(parse):
        # for record in self.data:
        #     if rec_date.strftime("%m/%d/%y") == record['date']: 
        #         field_data.append(record[field])

        # return field_data
    test_file = "house_info"
    test_class = "HouseInfo"
    test_method = "get_data_by_date"

    my_file = parse(test_file)
    assert my_file.success, my_file.message
    
    # my_class = house_info.class_(test_class)
    my_class = my_file.query("class {}(): ??".format(test_class))
    assert (
        my_class.exists()
    ), "Have you created a class called `{0}` in the `{1}` file?".format(test_class, test_file)

    my_method = my_file.class_(test_class).method(test_method)
    assert (
        my_method.exists()
    ), "Are you defining a method called `{}`?".format(test_method)
    
    # debug_test_case(my_method) 
    
    # assert False
    first_for = (
        my_method.for_().match(
            {

                "target_type": "Name",
                "target_id": "record",
                "iter_type": "Attribute",
                "iter_value_type": "Name",
                "iter_value_id": "self",
                "iter_attr": "data"
            }
        )
        .exists()
    )
    assert (
        first_for
    ), """Do you have a `for` loop, looping through `self.data`? 
        Is the current loop value called `record`?"""

    filter_recs = (
        my_method.for_().match(
            {
                "0_type": "If",
                "0_test_type": "Compare",
                "0_test_left_type": "Call",
                "0_test_left_func_type": "Attribute",
                "0_test_left_func_value_type": "Name",
                "0_test_left_func_value_id": "rec_date",
                "0_test_left_func_attr": "strftime",
                "0_test_left_args_0_type": "Constant",
                "0_test_left_args_0_value": "%m/%d/%y",
                "0_test_ops_0_type": "Eq",
                "0_test_comparators_0_type": "Subscript",
                "0_test_comparators_0_value_type": "Name",
                "0_test_comparators_0_value_id": "record",
                "0_test_comparators_0_slice_type": "Index",
                "0_test_comparators_0_slice_value_type": "Constant",
                "0_test_comparators_0_slice_value_value": "date",
                "0_body_0_type": "Expr",
                "0_body_0_value_type": "Call",
                "0_body_0_value_func_type": "Attribute",
                "0_body_0_value_func_value_type": "Name",
                "0_body_0_value_func_value_id": "field_data",
                "0_body_0_value_func_attr": "append",
                "0_body_0_value_args_0_type": "Subscript",
                "0_body_0_value_args_0_value_type": "Name",
                "0_body_0_value_args_0_value_id": "record",
                "0_body_0_value_args_0_slice_type": "Index",
                "0_body_0_value_args_0_slice_value_type": "Name",
                "0_body_0_value_args_0_slice_value_id": "field"

            }
        )
        .exists()
    )
    assert (
        filter_recs
    ), """Are you filtering the data using an `if` statement? 
        Are you converting the date format of `rec_date` to "%m/%d/%y" form?
        Are you casting the `rec_date` as string with `strptime()` when comparing with `rec['date']` field?
        Are you appending the filter records to `field_data`?"""


    # Test filer options:
    # recs = load_sensor_data()    # defined at top of file
    home_info = HouseInfo(recs)
    home_temp = home_info.get_data_by_date("id")
    assert (
        len(home_temp) == 0
    ), """The length of your filter data when calling `get_data_by_date` is incorrect.
        Your function call should have only one argument. For example: `id`
        Check the logic inside your loop"""

    rec_date = datetime.strptime("1/1/2020", "%m/%d/%Y")
    home_temp = home_info.get_data_by_date("id", rec_date)
    assert (
        len(home_temp) == 8
    ), """The length of your filter data when calling `get_data_by_date` is incorrect.
        Your call should have the first argument as `id`, 
            and the second argument as `datetime` object with the format: "%m/%d/%Y"
        Check the logic inside your loop"""
    
    rec_date = datetime.strptime("5/9/2020", "%m/%d/%Y")
    home_temp = home_info.get_data_by_date("id", rec_date)
    assert (
        len(home_temp) == 20
    ), """The length of your filter data when calling `get_data_by_date` is incorrect.
        Your call should have the first argument as `id`, 
            and the second argument as `datetime` object with the format: "%m/%d/%Y"
        Check the logic inside your loop"""
    

@pytest.mark.test_sensor_app_house_info_by_area_module2
def test_sensor_app_house_info_by_area_module2(parse):
    # from house_info import HouseInfo
    # ...
    # house_info = HouseInfo(data)
    # test_area = 1
    # recs = house_info.get_data_by_area("id", rec_area=test_area)
    # print("\nHouse sensor records for area {} = {}".format(test_area, len(recs)))

    test_file = "sensor_app"
    
    my_file = parse(test_file)
    assert my_file.success, my_file.message
    
    my_file_import = my_file.from_imports(
        "house_info", "HouseInfo")
    assert my_file_import, "Are you importing `HouseInfo` from `house_info` in `{}` file".format(test_file)

    # debug_test_case(my_file)    
    
    test_code = (
        my_file.assign_().match(
            {
                "2_type": "Assign",
                "2_targets_0_type": "Name",
                "2_targets_0_id": "house_info",
                "2_value_type": "Call",
                "2_value_func_type": "Name",
                "2_value_func_id": "HouseInfo",
                "2_value_args_0_type": "Name",
                "2_value_args_0_id": "data",
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Are you creating an instance of the class `HouseInfo` with 
        `data` list as the initialization argument for the constructor?
        """
    
    test_code = (
        my_file.assign_().match(
            {
        "3_type": "Assign",
        "3_targets_0_type": "Name",
        "3_targets_0_id": "test_area",
        "3_value_type": "Constant",
        "3_value_value": 1,
        "4_type": "Assign",
        "4_targets_0_type": "Name",
        "4_targets_0_id": "recs",
        "4_value_type": "Call",
        "4_value_func_type": "Attribute",
        "4_value_func_value_type": "Name",
        "4_value_func_value_id": "house_info",
        "4_value_func_attr": "get_data_by_area",
        "4_value_args_0_type": "Constant",
        "4_value_args_0_value": "id",
        "4_value_keywords_0_type": "keyword",
        "4_value_keywords_0_arg": "rec_area",
        "4_value_keywords_0_value_type": "Name",
        "4_value_keywords_0_value_id": "test_area",
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Are you creating a variable called `test_area` and setting it to 1?
          Are you creating a variable `recs` and setting it to `house_info.get_data_by_area()`?
          Are you passing `"id"` as the first argument to the method?
          Are you passing `rec_area=test_area` as the second argument to the method?"""


@pytest.mark.test_sensor_app_house_info_by_date_module2
def test_sensor_app_house_info_by_date_module2(parse):
    # from datetime import date, datetime
    # ...
    # test_date = datetime.strptime("5/9/20", "%m/%d/%y")
    # recs = house_info.get_data_by_date("id", rec_date = test_date)
    # print("House sensor records for {} = {}".format(test_date.date(), len(recs))) # (NOT TEST IT)

    test_file = "sensor_app"
    
    my_file = parse(test_file)
    assert my_file.success, my_file.message
    
    my_file_import = my_file.from_imports(
        "datetime", "datetime")
    assert my_file_import, "Are you importing `datetime` from `datetime` module?"

    my_file_import = my_file.from_imports(
        "datetime", "date")
    assert my_file_import, "Are you importing `date` from `datetime` module?"

    
    # debug_test_case(my_file)    
    
    test_code = (
        my_file.assign_().match(
            {
                "5_type": "Assign",
                "5_targets_0_type": "Name",
                "5_targets_0_id": "test_date",
                "5_value_type": "Call",
                "5_value_func_type": "Attribute",
                "5_value_func_value_type": "Name",
                "5_value_func_value_id": "datetime",
                "5_value_func_attr": "strptime",
                "5_value_args_0_type": "Constant",
                "5_value_args_0_value": "5/9/20",
                "5_value_args_1_type": "Constant",
                "5_value_args_1_value": "%m/%d/%y",
            }
        )
        .exists()
    )
    assert (
        test_code
    ),  """Are you creating an instance of the `datetime` class called `test_date` 

            which takes `"5/9/20"` and `"%m/%d/%y"` as the two arguments?"""
    
    test_code = (
        my_file.assign_().match(
            {
                "6_type": "Assign",
                "6_targets_0_type": "Name",
                "6_targets_0_id": "recs",
                "6_value_type": "Call",
                "6_value_func_type": "Attribute",
                "6_value_func_value_type": "Name",
                "6_value_func_value_id": "house_info",
                "6_value_func_attr": "get_data_by_date",
                "6_value_args_0_type": "Constant",
                "6_value_args_0_value": "id",
                "6_value_keywords_0_type": "keyword",
                "6_value_keywords_0_arg": "rec_date",
                "6_value_keywords_0_value_type": "Name",
                "6_value_keywords_0_value_id": "test_date",
            }
        )
        .exists()
    )
    assert (
        test_code
    ), """Are you creating a variable `recs` and setting it to `house_info.get_data_by_date()`?
          Are you passing `"id"` as the first argument to the method?
          Are you passing `rec_date=test_date` as the second argument to the method?"""
