import pytest
import json

import sensor.load_data
import sensor.house_info
from datetime import date, datetime


@pytest.mark.test_house_info_create_class_module2
def test_house_info_create_class_module2(parse):
    # class HouseInfo():
    #     def __init__(self, data):
    #         self.data = data

    house_info = parse("house_info")
    assert house_info.success, house_info.message

    house_info_class = house_info.class_("HouseInfo")
    assert (
        house_info_class.exists()
    ), "Have you created a class called `HouseInfo` in the `house_info.py` file?"

    class_init = house_info.class_("HouseInfo").method("__init__")
    assert class_init.exists(), "Are you defining a constructor called `__init__`?"
    
    class_init_q = house_info.query("class HouseInfo(): ??")
    test_method = "__init__"
    class_init_arguments= (
        class_init_q.def_args_(test_method).match(
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
        class_init_arguments
    ), """Are you defining a constructor for the `HouseInfo` class?
        Are you declaring the correct name and number of parameters?"""
    
    # Check for assignment 
    self_data_exists = (
        class_init_q.def_args_(test_method).match(
            {
                "body_0_type": "Assign",
                "body_0_targets_0_type": "Attribute",
                "body_0_targets_0_value_type": "Name",
                "body_0_targets_0_value_id": "self",
                "body_0_targets_0_attr": "data",
                "body_0_value_type": "Name",
                "body_0_value_id": "data",
            }
        )
        .exists()
    )
    assert (
        self_data_exists
    ), """Are you assigning the correct value to `self.data`?"""
    
    
@pytest.mark.test_house_info_get_data_by_area_module2
def test_house_info_get_data_by_area_module2(parse):
    
    # def get_data_by_area(self, field, rec_area=0):
        # field_data = []
    house_info = parse("house_info")
    assert house_info.success, house_info.message

    house_info_class = house_info.class_("HouseInfo")
    assert (
        house_info_class.exists()
    ), "Have you created a class called `HouseInfo` in the `house_info.py` file?"

    data_by_area = house_info.class_("HouseInfo").method("get_data_by_area")
    assert data_by_area.exists(), "Are you defining a method called `get_data_by_area?"

    test_method = "get_data_by_area"
    data_by_area_arguments= (
        house_info_class.def_args_(test_method).match(
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
        data_by_area_arguments
    ), """Are you defining a method `get_data_by_area` 
        with the correct name and number of parameters?
        Are you setting the third parameter's default value to zero?"""

    
    data_list = (
        data_by_area.assign_().match(
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
        data_list
    ), "Are you creating a variable called `field_data` set equal to an empty list?"


@pytest.mark.test_house_info_get_data_by_area_loop_module2
def test_house_info_get_data_by_area_loop_module2(parse):
    
    #     for record in self.data:
            # if rec_area == int(record['area']):       # select area
            #     field_data.append(record[field])
            # elif rec_area == 0:
            #     field_data.append(record[field])
    #     return field_data

    house_info = parse("house_info")
    assert house_info.success, house_info.message

    house_info_class = house_info.class_("HouseInfo")
    assert (
        house_info_class.exists()
    ), "Have you created a class called `HouseInfo` in the `house_info.py` file?"

    data_by_area = house_info.class_("HouseInfo").method("get_data_by_area")
    assert data_by_area.exists(), "Are you defining a method called `get_data_by_area?"

    test_method = "get_data_by_area"
    first_for = (
        data_by_area.for_().match(
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


    # Test filer options:
    recs = sensor.load_data.load_sensor_data()
    home_info = sensor.house_info.HouseInfo(recs)
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

    house_info = parse("house_info")
    assert house_info.success, house_info.message

    house_info_import = house_info.from_imports(
        "datetime", "date")
    assert house_info_import, "Are you importing `date` from datetime?"

    house_info_class = house_info.class_("HouseInfo")
    assert (
        house_info_class.exists()
    ), "Have you created a class called `HouseInfo` in the `house_info.py` file?"

    data_by_date = house_info.class_("HouseInfo").method("get_data_by_date")
    assert data_by_date.exists(), "Are you defining a method called `get_data_by_date?"
    
    test_method = "get_data_by_date"
    
    data_by_date_arguments= (
        house_info_class.def_args_(test_method).match(
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
        data_by_date_arguments
    ), """Are you defining a method `get_data_by_date` 
        with the correct name and number of parameters?
        Are you setting the third parameter's default value to date.today()?"""
    
    # print("1)", json.dumps(house_info_class.def_args_(test_method).n, indent=4))  # TODO Remove
    print("2)", json.dumps(data_by_date.assign_().n, indent=4))  # TODO Remove
    # assert False
    data_list = (
        data_by_date.assign_().match(
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
        data_list
    ), "Are you creating a variable called `field_data` set equal to an empty list?"
    
    
@pytest.mark.test_house_info_get_data_by_date_loop_module2
def test_house_info_get_data_by_date_loop_module2(parse):
        # for record in self.data:
        #     if rec_date.strftime("%m/%d/%y") == record['date']: 
        #         field_data.append(record[field])

        # return field_data
    house_info = parse("house_info")
    assert house_info.success, house_info.message

    house_info_class = house_info.class_("HouseInfo")
    assert (
        house_info_class.exists()
    ), "Have you created a class called `HouseInfo` in the `house_info.py` file?"

    test_method = "get_data_by_date"
    data_by_date = house_info.class_("HouseInfo").method(test_method)
    assert data_by_date.exists(), "Are you defining a method called `{}?".format(test_method)

    # print(json.dumps(data_by_date.for_().n, indent=2)) # TODO
    # assert False
    first_for = (
        data_by_date.for_().match(
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
        data_by_date.for_().match(
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
    recs = sensor.load_data.load_sensor_data()
    home_info = sensor.house_info.HouseInfo(recs)
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
    
    # print("1)", json.dumps(house_info_class.def_args_(test_method).n, indent=4))  # TODO Remove
    # print("2)", json.dumps(data_by_date.for_().n, indent=4))  # TODO Remove
    # assert False


@pytest.mark.test_sensor_app_house_info_by_area_module2
def test_sensor_app_load_house_info_by_area_module2(parse):
    # from house_info import HouseInfo
    # ...
    # house_info = HouseInfo(data)
    # recs = house_info.get_data_by_area("id", rec_area=1)
    # print("House sensor records for area 1 = {}".format(len(recs)))

    sensor = parse("sensor_app")
    assert sensor.success, sensor.message

    house_info_import = sensor.from_imports(
        "house_info", "HouseInfo")
    assert house_info_import, "Are you importing `HouseInfo` from house_info?"

    house_info = (
        sensor.assign_().match(
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
        house_info
    ), """Are you creating an instance of the `class` HouseInfo with 
        `data` list as the initialization argument for the constructor?
        """
    
    house_temp = (
        sensor.assign_().match(
            {
                "3_type": "Assign",
                "3_targets_0_type": "Name",
                "3_targets_0_id": "recs",
                "3_value_type": "Call",
                "3_value_func_type": "Attribute",
                "3_value_func_value_type": "Name",
                "3_value_func_value_id": "house_info",
                "3_value_func_attr": "get_data_by_area",
                "3_value_args_0_type": "Constant",
                "3_value_args_0_value": "id",
                "3_value_keywords_0_type": "keyword",
                "3_value_keywords_0_arg": "rec_area",
                "3_value_keywords_0_value_type": "Constant",
                "3_value_keywords_0_value_value": 1,
            }
        )
        .exists()
    )
    assert (
        house_temp
    ), """Are you creating a variable `recs` and setting it to the return 
            value from `house_info.get_data_by_area()`?
          Are you passing `area=1 or 2` as the second argument to the `get_data_by_area()` method?"""


@pytest.mark.test_sensor_app_house_info_by_date_module2
def test_sensor_app_load_house_info_by_date_module2(parse):
    # from datetime import date, datetime
    # ...
    # rec_date = datetime.strptime("5/9/2020", "%m/%d/%Y")
    # recs = house_info.get_data_by_date("id", rec_date)
    # print("House sensor records for {} = {}".format(rec_date.date(), len(recs)))

    sensor = parse("sensor_app")
    assert sensor.success, sensor.message

    datetime_import = sensor.from_imports(
        "datetime", "datetime")
    assert datetime_import, "Are you importing `datetime` from datetime?"

    date_import = sensor.from_imports(
        "datetime", "date")
    assert date_import, "Are you importing `date` from datetime?"
    # print(json.dumps(sensor.assign_().n, indent=2))
    # assert False

    house_date = (
        sensor.assign_().match(
            {
                "4_type": "Assign",
                "4_targets_0_type": "Name",
                "4_targets_0_id": "rec_date",
                "4_value_type": "Call",
                "4_value_func_type": "Attribute",
                "4_value_func_value_type": "Name",
                "4_value_func_value_id": "datetime",
                "4_value_func_attr": "strptime",
                "4_value_args_0_type": "Constant",
                "4_value_args_0_value": "5/9/2020",
                "4_value_args_1_type": "Constant",
                "4_value_args_1_value": "%m/%d/%Y",
            }
        )
        .exists()
    )
    assert (
        house_date
    ),  """Are you creating an instance of the datetime class called `record_date` 
            which takes "5/9/2020" and "%m/%d/%Y" as the two arguments?"""
    
    house_temp = (
        sensor.assign_().match(
            {
                "5_type": "Assign",
                "5_targets_0_type": "Name",
                "5_targets_0_id": "recs",
                "5_value_type": "Call",
                "5_value_func_type": "Attribute",
                "5_value_func_value_type": "Name",
                "5_value_func_value_id": "house_info",
                "5_value_func_attr": "get_data_by_date",
                "5_value_args_0_type": "Constant",
                "5_value_args_0_value": "id",
                "5_value_args_1_type": "Name",
                "5_value_args_1_id": "rec_date"
            }
        )
        .exists()
    )
    assert (
        house_temp
    ), """Are you creating a variable `recs` and setting it to the return 
            value from `house_info.get_data_by_date()`?
          Are you passing `area=1 or 2` as the second argument to the `get_data_by_area()` method?"""
