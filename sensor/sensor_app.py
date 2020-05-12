# Runner script for all modules
from load_data import load_sensor_data          # module 2

data = load_sensor_data()
# print(f"Loaded records {len(data)}")
print("Loaded records: [{}]".format(len(data)))