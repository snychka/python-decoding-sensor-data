from house_info import HomeData

# Module 4: Work with integer data from temperature sensor


class TemperatureData(HomeData):
    def get_data(self, field, room=0):
        field_info = self.get_data_by_room(field, room)
        data = []
        for rec in field_info:
            # Convert string of integers into actual integers based 10
            data.append(int(rec, 10))
        return data
