from load_info import load_sensor_data

# Module 3: Create an instance of sensor data


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
