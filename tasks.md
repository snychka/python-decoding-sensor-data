# Module 01 - The Sensor Class

- [Module 01 - The Sensor Class](#module-01---the-sensor-class)
  - [Status](#status)
  - [Module 1: Load Sensor Data From Files](#module-1-load-sensor-data-from-files)
    - [Task 1: Import os, glob, and csv](#task-1-import-os-glob-and-csv)
    - [Task 2: Create a Function to parse the data](#task-2-create-a-function-to-parse-the-data)
    - [Task 3: Set Python File Management](#task-3-set-python-file-management)
    - [Task 4: Read CSV Files](#task-4-read-csv-files)
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

The dataset for this project is stored in several CSV files found in the `dataset` folder. It represents the data collected from a device with multiple sensors. The records include measurements of temperature, humidity, energy consumption, and particle count in the air over a given area. The data is collected over a period of 24 hours.  

To start, open the file called `load_data.py` in the `sensor` folder - the rest of the tasks in this module happen in this same file.

At the top of the file create three import statements for `os`, `glob`, and `csv`. These libraries will allow us to work with a collection of files.

### Task 2: Create a Function to parse the data

[//]:# (@pytest.mark.test_load_data_load_sensor_func_module1)

Create a method called `load_sensor_data` that takes no arguments.
In the body of the `load_sensor_data` function, create variable called `sensor_data` and set it as an empty `list` - the rest of the tasks in this module happen in this function.

### Task 3: Set Python File Management

[//]:# (@pytest.mark.test_load_data_sensor_files_module1)

Below the `sensor_data` variable create another variable called `sensor_files` that is set to a call to the `glob.glob()` function.

Pass `glob` function a single argument, a call to the `os.path.join()` function. In turn pass `os.path.join()` three arguments: `os.getcwd()`, `datasets`, and `*.csv`.

The `datasets` argument corresponds to the folder with your sensor data. The data files are in `csv` format. You may open them and explore the content of the records in them.

### Task 4: Read CSV Files

[//]:# (@pytest.mark.test_load_data_load_sensor_func_module1)

## Module 2: Create a Class HomeData

## Module 3: Analyze Temperature Data

## Module 4: Analyze Humidity Data

## Module 5: Analyze Air Quality Data

## Module 6: Analyze Energy Consumption Data
