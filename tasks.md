# Module 01 - The Sensor Class

- [Module 01 - The Sensor Class](#module-01---the-sensor-class)
  - [Status](#status)
  - [Module 1: Load Sensor Data From Files](#module-1-load-sensor-data-from-files)
    - [Task 1: Import os, glob, and csv](#task-1-import-os-glob-and-csv)
    - [Task 2: Create a Function to parse the data](#task-2-create-a-function-to-parse-the-data)
  - [Module 2: Create a Class HomeData](#module-2-create-a-class-homedata)
  - [Module 3: Analyze Temperature Data](#module-3-analyze-temperature-data)
  - [Module 4: Analyze Humidity Data](#module-4-analyze-humidity-data)
  - [Module 5: Analyze Air Quality Data](#module-5-analyze-air-quality-data)
  - [Module 6: Analyze Energy Consumption Data](#module-6-analyze-energy-consumption-data)

## Status

Draft.

## Module 1: Load Sensor Data From Files

### Task 1: Import os, glob, and csv

[//]:# (@pytest.mark.test_load_data_function_module1)

```python
import os
import glob
import csv
```

The dataset for this project is stored in several CSV files found in the `dataset` folder. It represents the data collected from a device with multiple sensors. The records include measurements of temperature, humidity, energy consumption, and particle count in the air over a given area. The data is collected over a period of 24 hours.  

To start, open the file called `load_data.py` in the `sensor` folder - the rest of the tasks in this module happen in this same file.

At the top of the file create three import statements for `os`, `glob`, and `csv`. These libraries will allow us to work with a collection of files.

### Task 2: Create a Function to parse the data 

[//]:# (@pytest.mark.test_load_data_load_sensor_func_module1)

```python
def load_sensor_data():
  # create a list to store data
  sensor_data = []
```

Create a method called `load_sensor_data` that takes no arguments.
In the body of the `load_sensor_data` function, create variable called `sensor_data` and set it as an empty `list`.

## Module 2: Create a Class HomeData

## Module 3: Analyze Temperature Data

## Module 4: Analyze Humidity Data

## Module 5: Analyze Air Quality Data

## Module 6: Analyze Energy Consumption Data
