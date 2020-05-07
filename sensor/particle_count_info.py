from house_info import HomeData

# Module 6: Work with scientific notation data from Particle counter sensor


class ParticleData(HomeData):
    def get_data(self, field, room=0):
        field_info = self.get_data_by_room(field, room)
        data = []
        for rec in field_info:
            # Convert string of integers into floats
            data.append(float(rec))
        return data

    def get_concentrations(self, data):
        particulate = {"good": 0, "moderate": 0, "bad": 0}
        for rec in data:
            # Select particulate concentration
            if rec <= 50.0:
                particulate["good"] += 1
            elif rec > 50.0 and rec <= 100:
                particulate["moderate"] += 1
            else:
                particulate["bad"] += 1

        return particulate
