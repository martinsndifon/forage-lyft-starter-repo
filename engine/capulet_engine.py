from engine import Engine


class CapuletEngine(Engine):
    """Defines the Capulet engine"""

    def __init__(self, current_mileage, last_service_mileage):
        """Init"""
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        """Returns True if the engine needs servicing else false"""
        return self.current_mileage - self.last_service_mileage > 30000
