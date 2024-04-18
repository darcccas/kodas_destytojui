from datetime import datetime, timedelta

from driver import Driver


class Transport:
    def __init__(
        self,
        range_per_year: int = 100000,
        plate_number: str = "",
        fuel: str = "Diesel",
        costs: int = 1000,
        inspection_date: datetime = datetime(year=2024, month=6, day=30),
        driver=None,
        consumption_per_100km: float = 2.00,
        insurance_date: datetime = datetime(year=2024, month=4, day=30),
    ):
        if driver is None:
            driver = []
        self.consumption_per_100km = consumption_per_100km
        self.insurance_date = insurance_date
        self.driver = driver
        self.inspection_date = inspection_date
        self.costs = costs
        self.fuel = fuel
        self.plate_number = plate_number
        self.range_per_year = range_per_year
        self.costs_per_km = self.costs / self.range_per_year
        self.consumption_per_km = self.consumption_per_100km / 100

    def _valid_next_month(self, date: datetime):
        next_month = datetime.now().replace(day=1) + timedelta(days=32)
        return next_month.month == date.month and next_month.year == date.year

    def validate_date_insurance(self):
        return self._valid_next_month(self.insurance_date)

    def validate_date_inspection(self):
        return self._valid_next_month(self.inspection_date)

    def cost_per_trip(self, trip_range, fuel_price: float = 1.50):
        return (
            trip_range * self.consumption_per_km * fuel_price
            + trip_range * self.costs_per_km
        )

    def driver_on(self, driver: Driver):
        return (
            driver.off_time[0] < datetime.now() and driver.off_time[1] > datetime.now()
        )

    def driver_license(self, driver: Driver):
        return self.driver[0] in driver.can_drive
