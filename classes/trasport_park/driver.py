from datetime import datetime


class Driver:
    def __init__(self, off_time=None, can_drive=None, earnings: int = 0.50):
        if can_drive is None:
            can_drive = ["B", "C", "CE"]
        if off_time is None:
            off_time = [
                datetime(year=2024, month=4, day=1),
                datetime(year=2024, month=5, day=1),
            ]
        self.earnings = earnings
        self.can_drive = can_drive
        self.off_time = off_time
