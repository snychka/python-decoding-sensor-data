import pytest
import json


@pytest.mark.test_load_data_import_module1
def test_load_data_import_module1(parse):

    # import os
    # import glob
    # import csv

    load_data = parse("load_data")
    assert load_data.success, load_data.message

    os_import = load_data.imports("os")
    assert os_import, "Are you importing `os`?"

    glob_import = load_data.imports("glob")
    assert glob_import, "Are you importing `glob`?"

    csv_import = load_data.imports("csv")
    assert csv_import, "Are you importing `csv`?"


@pytest.mark.test_load_data_load_sensor_func_module1
def test_load_data_load_sensor_func_module1(parse):

    # def load_sensor_data():
    #     sensor_data = []

    load_data = parse("load_data")
    assert load_data.success, load_data.message

    load_sensor_data = load_data.defines("load_sensor_data")
    assert (
        load_sensor_data.exists()
    ), "Are you defining a function called `load_sensor_data` with the correct arguments?"

    # print(json.dumps(load_sensor_data.assign_().n, indent=2))
    # assert False

    sensor_data = load_sensor_data.assign_().match(
        {
            "type": "Assign",
            "targets_0_type": "Name",
            "targets_0_id": "sensor_data",
            "value_type": "List",
        }
    )
    assert (
        sensor_data
    ), "Are you creating a variable called `sensor_data` set equal to an empty list?"


@pytest.mark.test_load_data_sensor_files_module1
def test_load_data_sensor_files_module1(parse):

    # def load_sensor_data():
    #   ....
    #   sensor_files = glob.glob(os.path.join(os.getcwd(), 'datasets', '*.csv'))

    load_data = parse("load_data")
    assert load_data.success, load_data.message

    # load_sensor_data = load_data.query("def load_sensor_data(): ??")
    load_sensor_data = load_data.defines("load_sensor_data")
    load_sensor_data_exists = load_sensor_data.exists()
    assert (
        load_sensor_data_exists
    ), "Are you defining a function called `load_sensor_data` with the correct arguments?"

    sensor_files = (
        load_sensor_data.assign_()
        .match(
            {
                "1_type": "Assign",
                "1_targets_0_type": "Name",
                "1_targets_0_id": "sensor_files",
                "1_value_type": "Call",

                "1_value_func_type": "Attribute",
                "1_value_func_value_type": "Name",
                "1_value_func_value_id": "glob",
                "1_value_func_attr": "glob",

                "1_value_args_0_type": "Call",
                "1_value_args_0_func_type": "Attribute",
                "1_value_args_0_func_value_type": "Attribute",
                "1_value_args_0_func_value_value_type": "Name",
                "1_value_args_0_func_value_value_id": "os",
                "1_value_args_0_func_value_attr": "path",
                "1_value_args_0_func_attr": "join",

                "1_value_args_0_args_0_type": "Call",
                "1_value_args_0_args_0_func_type": "Attribute",
                "1_value_args_0_args_0_func_value_type": "Name",
                "1_value_args_0_args_0_func_value_id": "os",
                "1_value_args_0_args_0_func_attr": "getcwd",
                "1_value_args_0_args_1_type": "Constant",
                "1_value_args_0_args_1_value": "datasets",
                "1_value_args_0_args_2_type": "Constant",
                "1_value_args_0_args_2_value": "*.csv"
            }
        )
        .exists()
    )
    assert (
        sensor_files
    ), "Are you creating a variable called `sensor_files` and assigning it glob.glob() and passing os.path.join()? Are you passing 3 values to os.path.join()?"


# @pytest.mark.test_load_data_sensor_files_query_module1
# def test_load_data_sensor_files_query_module1(parse):

#     # def load_sensor_data():
#     #   ....
#     #   sensor_files = glob.glob(os.path.join(os.getcwd(), 'datasets', '*.csv'))

#     load_data = parse("load_data")
#     assert load_data.success, load_data.message

#     sensor_files = load_data.query(
#         "glob.glob(os.path.join(os.getcwd(), 'datasets', '*.csv'))")
#     sensor_files_exists = sensor_files.exists()
#     assert (
#         sensor_files_exists
#     ), "Are you including `glob.glob(os.path.join(os.getcwd(), 'datasets', '*.csv'))` in your code?"


@pytest.mark.test_load_data_read_files_module1
def test_load_data_read_files_module1(parse):

    # def load_sensor_data():
    #   ....
    # for sensor_file in sensor_files:
    #     with open(sensor_file) as data_file:
    #         data_reader = csv.DictReader(data_file, delimiter=',')
    #         for row in data_reader:
    #             sensor_data.append(row)
    # return sensor_data

    load_data = parse("load_data")
    assert load_data.success, load_data.message

    # load_sensor_data = load_data.defines("load_sensor_data")
    load_sensor_data = load_data.query("def load_sensor_data(): ??")
    assert (
        load_sensor_data.exists()
    ), "Are you defining a function called `load_sensor_data` with the correct arguments?"

    # print(json.dumps(load_sensor_data.for_().n, indent=2))  # TODO Remove
    # print(json.dumps(load_sensor_data.assign_().n, indent=2))
    # print(json.dumps(load_sensor_data.returns_call().n, indent=2))
    # print(json.dumps(load_sensor_data.assigns().n, indent=2))
    # assert False

    first_for_exists = (
        load_sensor_data.for_()
        .match(
            {
                "target_type": "Name",
                "target_id": "sensor_file",
                "iter_type": "Name",
                "iter_id": "sensor_files",
            }
        )
        .exists()
    )
    assert (
        first_for_exists
    ), 'Do you have a `for` loop, looping through `sensor_files`? Is the current loop value called `sensor_file`?'

    with_exists = (
        load_sensor_data.for_()
        .match(
            {
                "0_type": "With",
                "0_items_0_type": "withitem",
                "0_items_0_context_expr_type": "Call",
                "0_items_0_context_expr_func_type": "Name",
                "0_items_0_context_expr_func_id": "open",
                "0_items_0_context_expr_args_0_type": "Name",
                "0_items_0_context_expr_args_0_id": "sensor_file",
                "0_items_0_optional_vars_type": "Name",
                "0_items_0_optional_vars_id": "data_file"
            }
        )
        .exists()
    )
    assert (
        with_exists
    ), "Do you have a call to `open` in your `with` code and are you passing `open` the correct argument?"

    data_reader = (
        load_sensor_data.for_()
        .match(
            {
                "0_body_0_type": "Assign",
                "0_body_0_targets_0_type": "Name",
                "0_body_0_targets_0_id": "data_reader",
                "0_body_0_value_type": "Call",
                "0_body_0_value_func_type": "Attribute",
                "0_body_0_value_func_value_type": "Name",
                "0_body_0_value_func_value_id": "csv",
                "0_body_0_value_func_attr": "DictReader",
                "0_body_0_value_args_0_type": "Name",
                "0_body_0_value_args_0_id": "data_file",
                "0_body_0_value_keywords_0_type": "keyword",
                "0_body_0_value_keywords_0_arg": "delimiter",
                "0_body_0_value_keywords_0_value_type": "Constant",
                "0_body_0_value_keywords_0_value_value": ",",
            }
        )
        .exists()
    )
    assert (
        data_reader
    ), "Are you assigning `data_reader` the result of `csv.DictReader()` with the correct input argument and delimeter?"

    second_for_exist = (
        load_sensor_data.for_()
        .match(
            {
                "0_body_1_type": "For",
                "0_body_1_target_type": "Name",
                "0_body_1_target_id": "row",
                "0_body_1_iter_type": "Name",
                "0_body_1_iter_id": "data_reader",
            }
        )
        .exists()
    )
    assert (
        second_for_exist
    ), 'Do you have a second `for` loop, looping through `data_reader`? Is the current loop value called `row`?'

    sensor_data_append = (
        load_sensor_data.for_()
        .match(
            {
                "0_body_1_body_0_type": "Expr",
                "0_body_1_body_0_value_type": "Call",
                "0_body_1_body_0_value_func_type": "Attribute",
                "0_body_1_body_0_value_func_value_type": "Name",
                "0_body_1_body_0_value_func_value_id": "sensor_data",
                "0_body_1_body_0_value_func_attr": "append",
                "0_body_1_body_0_value_args_0_type": "Name",
                "0_body_1_body_0_value_args_0_id": "row"
            }
        )
        .exists()
    )
    assert (
        sensor_data_append
    ), 'Are you appending the `row` records to the `sensor_data` list?'

    returns_load_sensor_data = load_sensor_data.returns("sensor_data")
    assert (
        returns_load_sensor_data
    ), 'Are you returning `sensor_data` from `load_sensor_data` function?'


@pytest.mark.test_sensor_app_load_data_return_module1
def test_sensor_app_load_data_return_module1(parse):
    # from load_data import load_sensor_data
    # data = load_sensor_data()
    # print("Loaded records {}".format(len(data)))

    sensor = parse("sensor_app")
    assert sensor.success, sensor.message

    load_sensor_data_import = sensor.from_imports(
        "load_data", "load_sensor_data")
    assert load_sensor_data_import, "Are you importing `load_sensor_data` from load_data?"

    # print(json.dumps(sensor.assign_().n, indent=2))
    # print(json.dumps(sensor.calls().n, indent=2))
    # assert False

    data = sensor.assign_().match(
        {
            "type": "Assign",
            "targets_0_type": "Name",
            "targets_0_id": "data",
            "value_type": "Call",
            "value_func_type": "Name",
            "value_func_id": "load_sensor_data",
        }
    )
    assert (
        data
    ), "Are you creating a variable called `data` set equal to `load_sensor_data()` function?"

    print_data = sensor.calls().match(
        {
            "type": "Expr",
            "value_type": "Call",
            "value_func_type": "Name",
            "value_func_id": "print",
            "value_args_0_type": "Call",
            "value_args_0_func_type": "Attribute",
            "value_args_0_func_value_type": "Constant",
            "value_args_0_func_value_value": "Loaded records {}",
            "value_args_0_func_attr": "format",
            "value_args_0_args_0_type": "Call",
            "value_args_0_args_0_func_type": "Name",
            "value_args_0_args_0_func_id": "len",
            "value_args_0_args_0_args_0_type": "Name",
            "value_args_0_args_0_args_0_id": "data"
        }
    )
    assert (
        print_data
    ), "Are you calling `print()` and passing in `format()`? Are you passing 1 values to `format()` `len(data)`"
