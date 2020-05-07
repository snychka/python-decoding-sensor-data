from house_info import HomeData

# Module 5: Work with floating point data from humidity sensor


class HumidityData(HomeData):
    def get_data(self, field, room=0):
        field_info = self.get_data_by_room(field, room)
        data = []
        for rec in field_info:
            # Convert string of integers into floats
            data.append(float(rec) * 100)
        return data
