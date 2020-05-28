# Runner script for all modules
from load_data import load_sensor_data
from house_info import HouseInfo
from datetime import datetime, date
##############################
# Do not remove these two lines
# They are needed to validate your unittest
data = []
print("Sensor Data App")
##############################

# Module 1 code here:
data = load_sensor_data()
print("Loaded records: {}".format(len(data)))
# Module 2 code here:
house_info = HouseInfo(data)
test_area = 1
recs = house_info.get_data_by_area("id", rec_area=test_area)
print("\nHouse sensor records for area {} = {}".format(test_area, len(recs)))

test_date = datetime.strptime("5/9/20", "%m/%d/%y")
recs = house_info.get_data_by_date("id", rec_date=test_date)
print("House sensor records for date {} = {}".format(test_date.strftime("%m/%d/%y"), len(recs)))

# Module 3 code here:

# Module 4 code here:

# Module 5 code here: