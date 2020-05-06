import os
import glob
import csv
from collections import defaultdict

# Set file(s) path
sensor_files = glob.glob(os.path.join(os.getcwd(), 'datasets', '*.csv'))
sensor_files.sort()

line_count = 0

sensor_data = defaultdict(list)
# Loop over list of files
for sensor_file in sensor_files:
    with open (sensor_file) as data_file:
        # Create a csv.DictReader
        data_reader = csv.DictReader(data_file, delimiter=',')
        # Loop over each row dictionary
        for row in data_reader: 

            # Method 1: Create a manual dictionary of lists
            # sensor_data['id'].append(row['id'])
            # sensor_data['date'].append(row['date'])
            # sensor_data['time'].append(row['time'])
            # sensor_data['temperature'].append(row['temperature'])
            # sensor_data['humidity'].append(row['humidity'])
            # sensor_data['particle_count_hex'].append(row['particle_count_hex'])
            # sensor_data['particle_count_sn'].append(row['particle_count_sn'])
            
            # Method 2: Loop over dictionary to create dictionary of lists
            for key in row:
                sensor_data[key].append(row[key])
            line_count += 1

print(f'Processed {line_count} lines.')
print(sensor_data.keys())