from datetime import datetime
from math import ceil

from classes.trasport_park.transport import Transport


class Truck(Transport):
    def __init__(
        self,
        truck_load: int = 12000,
        range_per_year: int = 200000,
        plate_number: str = "",
        fuel: str = "Diesel",
        costs: int = 3000,
        inspection_date: datetime = datetime(year=2024, month=6, day=30),
        driver=None,
        consumption_per_100km: float = 29.00,
        insurance_date: datetime = datetime(year=2024, month=4, day=30),
        trailer: bool = True,
        trailer_load: int = 5000,
    ):

        super().__init__(
            range_per_year,
            plate_number,
            fuel,
            costs,
            inspection_date,
            driver,
            consumption_per_100km,
            insurance_date,
        )

        if driver is None:
            driver = ["CE"]
        self.driver = driver
        self.trailer_load = trailer_load
        self.truck_load = truck_load
        self.trailer = trailer
        self.truck_trailer = self.truck_load + self.trailer_load

    def calculate_trucks_needed(self, cargo_weight: int = 36000):
        trucks = ceil(cargo_weight / self.truck_trailer)
        if self.trailer_load * trucks >= cargo_weight:
            trailers = ceil(
                (cargo_weight - self.truck_load * trucks) / self.trailer_load
            )
        else:
            trailers = 0
        return trucks, trailers
