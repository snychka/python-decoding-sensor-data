from house_info import HomeData

# Module 7: Work with hex and binary data from light bulbs sensor to energy

ENERGY_PER_BULB = 0.2        # in watts
ENERGY_BITS = 0x0F0


class EnergyData(HomeData):
    def get_data(self, field, room=0):
        field_info = self.get_data_by_room(field, room)
        data = []
        for rec in field_info:
            # Convert string hex to binary
            data.append(bin(int(rec, 16)))
        return data

    def calculate_energy_usage(self, data):
        total_energy = 0
        for rec in data:
            # Convert string to hex
            rec = int(rec, 2)
            rec = rec & ENERGY_BITS                 # mask ENERGY bits
            rec = rec >> 4                          # shift right
            total_energy += rec * ENERGY_PER_BULB   # calculate energy
        return total_energy
