import os, glob, csv

'''
1. Create one `for` loop that loops through `sensor_files` using `sensor_file` as the iterator variable. 

1. In the body of this loop use a `with` statement to `open` the `sensor_file` and set the alias to `data_file`.

1. In the `with` body, set a variable called `data_reader` equal to `csv.DictReader()`. Pass in the current `data_file` as the first argument, and set the `delimiter=','` as the second argument. The `data_reader` will contain a list of dictionaries with the sensor data. 

1. Create a second `for` loop to `data_file` to get access to each record. Use `row` as your iterator variable. 

1. Inside the body of the second `for` loop, append each `row` record to the `sensor_data` list created on `Task 2`

Finally, your function should return `sensor_data` list containing a list of dictionaries.
'''
def load_sensor_data():
    sensor_data = []
    sensor_files = glob.glob(os.path.join(os.getcwd(), "datasets", "*.csv"))

    for sensor_file in sensor_files:
        with open(sensor_file) as data_file:
            data_reader = csv.DictReader(data_file, delimiter=',')
            for row in data_reader:
                sensor_data.append(row)

    return sensor_data
