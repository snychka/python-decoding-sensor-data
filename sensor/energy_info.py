from house_info import HouseInfo
from datetime import datetime, date

class EnergyData(HouseInfo):

    ENERGY_PER_BULB = 0.2
    ENERGY_BITS = 0x0F0

    def _get_energy(self, rec):
        rec  = int(rec, 16)
        rec = rec & self.ENERGY_BITS
        rec = rec >> 4
        return rec

    def _convert_data(self, data):
        recs = []
        for rec in data:
            recs.append(self._get_energy(rec))
        return recs

    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("energy_usage", rec_area)
        return self._convert_data(recs)

    def get_data_by_date(self, rec_date=date.today()):
        recs = super().get_data_by_date("energy_usage", rec_date)
        return self._convert_data(recs)

    def calculate_energy_usage(self, data):
        total_energy = sum([field * self.ENERGY_PER_BULB for field in data])
        return total_energy
