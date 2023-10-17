from serviceable import Serviceable


class Car(Serviceable):
    """A class for all new cars"""
    def __init__(self, battery, engine):
        self.battery = battery
        self.engine = engine

    def needs_service(self):
        """Returns True if either of the service requirements needs service"""
        return self.battery.needs_service() or self.engine.needs_service()
