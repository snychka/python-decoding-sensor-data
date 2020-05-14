# Runner script for all modules
from load_data import load_sensor_data          # module 2
from house_info import HouseInfo
from datetime import date, datetime

# Do not remove these two lines
# if you do, it will break the unittest
recs = 0
print("Sensor Data App")

recs = load_sensor_data()
# print(f"Loaded records {len(data)}")
print("Loaded records: [{}]".format(len(recs)))

house_info = HouseInfo(data)
recs = house_info.get_data_by_area("id", area=1)
print("House sensor records for area 1 = {}".format(
       len(recs)))

rec_date = datetime.strptime("5/9/2020", "%m/%d/%Y")
recs = house_info.get_data_by_date("id", rec_date)
print("House sensor records for {} = {}".format(
       rec_date.date(), len(recs)))