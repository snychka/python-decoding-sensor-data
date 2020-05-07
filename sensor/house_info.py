from sensor_data import sensor_data

# Module 3: Work with integer data
class HomeData(object):
        def __init__(self, data):
                self.data = data
        
        def get_data_by_room(self, field, room=0):
                data = []
                # loop over records
                for record in self.data:
                        # filter data by room
                        if room == 0:                           # take all room
                                data.append(record[field])
                        elif room == int(record['room']):       # select room
                                data.append(record[field])
                return data
        


home_info = HomeData(sensor_data)
home_temp = home_info.get_data_by_room("temperature")
print(f"Home temperature records {len(home_temp)}" )