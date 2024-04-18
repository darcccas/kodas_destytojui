from datetime import datetime, timedelta

from classes.trasport_park.transport import Transport


class Car(Transport):
    def __init__(
        self,
        range_per_year: int = 30000,
        plate_number: str = "EA1548",
        fuel: str = "Electricity",
        costs: int = 700,
        inspection_date: datetime = datetime(year=2024, month=5, day=30),
        driver=None,
        consumption_per_100km: float = 16.00,
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
            driver = ["B"]
        self.driver = driver
