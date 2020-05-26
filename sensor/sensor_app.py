from house_info import HouseInfo
from load_data import load_sensor_data 
from datetime import datetime, date
from temperature_info import TemperatureData

# don't remove
data = []
print("Sensor Data App")

data = load_sensor_data()
#data = []
#print(f'Loaded records: [{data}]')
print('Loaded records: {0}'.format(len(data)))

house_info = HouseInfo(data)

recs = house_info.get_data_by_area('id', rec_area=1)
print('House sensor records for area 1 = {0}'.format(len(recs)))
#rec_date = datetime.strptime("5/9/2020" , "%m/%d/%Y")
#record_date = datetime.strptime("5/9/20" , "%m/%d/%y")
test_date = datetime.strptime("5/9/20" , "%m/%d/%y")
#recs = house_info.get_data_by_date("id", rec_date)
#recs = house_info.get_data_by_date("id", record_date)
recs = house_info.get_data_by_date("id", rec_date=test_date)
print('House sensor records for 2020-05-09 = {0}'.format(len(recs)))

temperature_data = TemperatureData(data)
recs = temperature_data.get_data_by_area(rec_area=1)
print("\nHouse Temperature sensor records for area 1 = {}".format(len(recs)))
print("\tMaximum: {0}, Minimum: {1} temperatures".format(max(recs), min(recs)))

recs = temperature_data.get_data_by_date(rec_date=test_date)
print("\nHouse Temperature sensor records for area 1 = {}".format(len(recs)))
print("\tMaximum: {0}, Minimum: {1} temperatures".format(max(recs), min(recs)))
