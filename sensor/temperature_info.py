import matplotlib.pyplot as plt
from statistics import mean
from sensor_data import sensor_data
from house_info import HomeData

# Module 4: Work with integer data
class TemperatureData(HomeData):
        def get_data(self, field, room=0):
                field_info = self.get_data_by_room(field, room)
                data = []
                for rec in field_info:
                        # Convert string of integers into actual integers based 10
                        data.append(int(rec, 10))
                return data

home_temp = TemperatureData(sensor_data)
room1_temp = home_temp.get_data("temperature", 1)
room2_temp = home_temp.get_data("temperature", 2)
rooms_temp = home_temp.get_data("temperature")
print(f"Max Room 1 {max(room1_temp)}, min {min(room1_temp)}, avg {mean(room1_temp)}, records {len(room1_temp)}" )
print(f"Max Room 2 {max(room2_temp)}, min {min(room2_temp)}, avg {mean(room2_temp)}, records {len(room2_temp)}" )
print(f"Max Rooms  {max(rooms_temp)}, min {min(rooms_temp)}, avg {mean(rooms_temp)}, records {len(rooms_temp)}" )

# # Sort both list
# temperatures, temp_times = zip(*sorted(zip(temperatures, temp_times)))
# # Plot the date
# fig, ax = plt.subplots()
# ax.plot(temp_times, temperatures, 'o')
# # ax.plot(temp_times, temperatures, style='k.')

# ax.set(xlabel='time (s)', ylabel='temperature in C',
#        title='About as simple as it gets, folks')
# ax.grid()

# # fig.savefig("test.png")
# plt.show()