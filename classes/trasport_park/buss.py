from datetime import datetime
from math import ceil

from classes.trasport_park.transport import Transport


class Buss(Transport):
    def __init__(
        self,
        seats: int = 35,
        range_per_year: int = 100000,
        plate_number: str = "ABA 457",
        fuel: str = "Diesel",
        costs: int = 1200,
        inspection_date: datetime = datetime(year=2024, month=5, day=30),
        driver=None,
        consumption_per_100km: float = 15.50,
        insurance_date: datetime = datetime(year=2024, month=5, day=30),
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
            driver = ["D"]
        self.driver = driver
        self.seats = seats

    def busses_need(self, number_of_pas):
        try:
            return ceil(number_of_pas / self.seats)
        except ZeroDivisionError as e:
            print(f"Klaida:{e}")

    def buss_trip_cost(self, number_of_pas, trip_range, fuel_cost: float = 1.50):
        return self.cost_per_trip(trip_range, fuel_cost) * self.busses_need(
            number_of_pas
        )
