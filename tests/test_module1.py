
import re
import pytest


@pytest.mark.test_site_sys_import_module1
def test_site_sys_import_module1(parse):
    # import sys

    # test file exist
    sensor = parse("load_info")
    assert sensor.success, sensor.message

    # test import sys
    sys_import = "sys" in sensor.get_imports()
    assert sys_import, "Have you imported `sys`?"