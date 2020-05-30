from house_info import HouseInfo
from load_data import load_sensor_data 
from datetime import datetime, date
from temperature_info import TemperatureData
from humidity_info import HumidityData
from statistics import mean
from particle_count_info import ParticleData
from energy_info import EnergyData

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

humidity_data = HumidityData(data)
recs = humidity_data.get_data_by_area(rec_area=1)
print("\nHouse Humidity sensor records for area 1 = {}".format(len(recs)))
print("\tAverage: {} humidity".format(mean(recs)))

recs = humidity_data.get_data_by_date(rec_date=test_date)
print("House Humidity sensor records for date: {} = {}".format( test_date.strftime("%m/%d/%y"), len(recs)))
print("\tAverrage: {} humdity".format(mean(recs)))

particle_data = ParticleData(data)
recs = particle_data.get_data_by_area(rec_area=1)
print("\nHouse Particle sensor records for area 1 = {}".format(len(recs)))
concentrations = particle_data.get_data_concentrations(data=recs)
print("\tGood Air Quality Recs: {}".format(concentrations["good"]))
print("\tModerate Air Quality Recs: {}".format(concentrations["moderate"]))
print("\tBad Air Quality Recs: {}".format(concentrations["bad"]))

recs = particle_data.get_data_by_date(rec_date=test_date)
print("\nHouse Particle sensor records for date: {} = {}".format( test_date.strftime("%m/%d/%y"), len(recs)))
concentrations = particle_data.get_data_concentrations(data=recs)
print("\tGood Air Quality Recs: {}".format(concentrations["good"]))
print("\tModerate Air Quality Recs: {}".format(concentrations["moderate"]))
print("\tBad Air Quality Recs: {}".format(concentrations["bad"]))

energy_data = EnergyData(data)
recs = energy_data.get_data_by_area(rec_area=1)
print("\nHouse Energy sensor records for area 1 = {}".format(len(recs)))
total_energy = energy_data.calculate_energy_usage(data=recs)
print("\tEnergy Usage: {:2.2} Watts".format(total_energy))

recs = energy_data.get_data_by_date(rec_date=test_date)
print("House Energy sensor records for date: {} = {}".format( test_date.strftime("%m/%d/%y"), len(recs)))
total_energy = energy_data.calculate_energy_usage(data=recs)
print("\tEnergy Usage: {:2.2} Watts".format(total_energy))
