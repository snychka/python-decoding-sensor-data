# Module 1 - The Sensor Class

- [Module 1 - The Sensor Class](#module-1---the-sensor-class)
  - [Status](#status)
  - [Module 1: Load Sensor Data From Files](#module-1-load-sensor-data-from-files)
    - [M1: Task 1: Import os, glob, and csv](#m1-task-1-import-os-glob-and-csv)
    - [M1: Task 2: Create a Function to parse the data](#m1-task-2-create-a-function-to-parse-the-data)
    - [M1: Task 3: Sensor Data File Management](#m1-task-3-sensor-data-file-management)
    - [M1: Task 4: Read Data Files](#m1-task-4-read-data-files)
    - [M1: Task 5: Get Sensor Data with sensor_app](#m1-task-5-get-sensor-data-with-sensorapp)
  - [Module 2: Create a Class HomeData](#module-2-create-a-class-homedata)
  - [Module 3: Analyze Temperature Data](#module-3-analyze-temperature-data)
  - [Module 4: Analyze Humidity Data](#module-4-analyze-humidity-data)
  - [Module 5: Analyze Air Quality Data](#module-5-analyze-air-quality-data)
  - [Module 6: Analyze Energy Consumption Data](#module-6-analyze-energy-consumption-data)

## Status

Draft.

## Module 1: Load Sensor Data From Files

### M1: Task 1: Import os, glob, and csv

[//]:# (@pytest.mark.test_load_data_import_module1)

The dataset for this project is stored in several CSV files found in the `dataset` folder. It represents the data collected from a device with multiple sensors. The records include measurements of temperature, humidity, energy consumption, and particle count in the air over a given area. The data is collected over a period of 24 hours.  

To start, open the file called `load_data.py` in the `sensor` folder - the rest of the tasks in this module happen in this same file.

At the top of the file create three import statements for `os`, `glob`, and `csv`. These libraries will allow us to work with a collection of files.

---
To test this module locally:

- Open a terminal at the root of the project
- Run the command `pytest -k module1`

### M1: Task 2: Create a Function to parse the data

[//]:# (@pytest.mark.test_load_data_load_sensor_func_module1)

Create a function called `load_sensor_data` that takes no arguments.
In the body of the `load_sensor_data` function, create variable called `sensor_data` and set it as an empty `list`.

---
To test this module locally:

- Open a terminal at the root of the project
- Run the command `pytest -k module1`

### M1: Task 3: Sensor Data File Management

[//]:# (@pytest.mark.test_load_data_sensor_files_module1)

Next, create a variable called `sensor_files` that is set to a call to the `glob.glob()` function.

Pass the glob function a single argument, a call to the `os.path.join()` function.

In turn pass `os.path.join()` three arguments: `os.getcwd()`, `"datasets"`, and `"*.csv"`.

Your statement should look like this:

```python
    sensor_files = glob.glob(os.path.join(os.getcwd(), 'datasets', '*.csv'))
```

---
To test this module locally:

- Open a terminal at the root of the project
- Run the command `pytest -k module1`

### M1: Task 4: Read Data Files

[//]:# (@pytest.mark.test_load_data_read_files_module1)

The `sensor_files` object contains a list of file names i.e. ['SENSOR_ROOM2', 'SENSOR_ROOM1']

To read the sensor data of these files, five steps are required:

1) Create one `for` loop that loops through `sensor_files` using `sensor_file` as the iterator variable.

2) In the body of this loop use a `with` statement to `open` the `sensor_file` and set the alias to `data_file`.

3) In the `with` body, set a variable called `data_reader` equal to `csv.DictReader()`. Pass in the current `data_file` as the first argument, and set the `delimiter=','` as the second argument. The `data_reader` will contain a list of dictionaries with the sensor data.

4) Create a second `for` loop to `data_file` to get access to each record. Use `row` as your iterator variable.

5) Inside the body of the second `for` loop, append each `row` record to the `sensor_data` list created on `Task 2`

Finally, your function should return `sensor_data` list containing a list of dictionaries.

---
To test this module locally:

- Open a terminal at the root of the project
- Run the command `pytest -k module1`

### M1: Task 5: Get Sensor Data with sensor_app

[//]:# (@pytest.mark.test_sensor_app_load_data_return_module1)
oLet's set up the command line interface (CLI). Open the `sensor_app.py` file in the `sensor` directory of the project.

At the top,  from the `load_data` module, `import` the `load_sensor_data` function.

Define variable called `data` and set it equal to `load_sensor_data()`.

Print the length of the `data` list using `formatted` print. Your output should look like this:

```bash
Loaded records: [2000]
```

---
To test this task locally:

- Open a terminal at the root of the project
- Run the command `python sensor/sensor_app.py`

---
To test this module locally:

- Open a terminal at the root of the project
- Run the command `pytest -k module1`

-

## Module 2: Create a Class HomeData

## Module 3: Analyze Temperature Data

## Module 4: Analyze Humidity Data

## Module 5: Analyze Air Quality Data

## Module 6: Analyze Energy Consumption Data
