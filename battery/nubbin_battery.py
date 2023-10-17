from battery import Battery
from utils import add_years_to_date


class NubbinBattery(Battery):
    """Defines the Nubbin Battery"""

    def __init__(self, last_service_date, current_date):
        """Initialize the class"""
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        """Returns True if the battery needs servicing else false"""
        battery_threshold_date = add_years_to_date(self.last_service_date, 4)
        if battery_threshold_date < self.current_date:
            return True
        else:
            return False
