import pytest
import json


@pytest.mark.test_load_data_import_module1
def test_load_data_import_module1(parse):

    # import os
    # import glob
    # import csv

    load_data = parse("load_data")
    assert load_data.success, load_data.message

    sys_import = load_data.imports("os")
    assert sys_import, "Are you importing `os`?"

    sys_import = load_data.imports("glob")
    assert sys_import, "Are you importing `glob`?"

    sys_import = load_data.imports("csv")
    assert sys_import, "Are you importing `csv`?"


@pytest.mark.test_load_data_load_sensor_func_module1
def test_load_data_load_sensor_func_module1(parse):

    # def load_sensor_data():
    #     sensor_data = []

    load_data = parse("load_data")
    assert load_data.success, load_data.message

    load_sensor_data = load_data.query("def load_sensor_data(): ??")
    load_sensor_data_exists = load_sensor_data.exists()
    assert (
        load_sensor_data_exists
    ), "Are you defining a function called `load_sensor_data` with the correct arguments?"

    sensor_data = (
        load_sensor_data.assign_()
        .match(
            {
                "type": "Assign",
                "targets_0_type": "Name",
                "targets_0_id": "sensor_data",
                "value_type": "List",
            }
        )
        .exists()
    )
    assert (
        sensor_data
    ), "Are you creating a variable called `sensor_data` set equal to an empty list?"
