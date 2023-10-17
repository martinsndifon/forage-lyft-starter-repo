from engine.engine import Engine


class SternmanEngine(Engine):
    """Defines the Capulet engine"""

    def __init__(self, warning_light_on):
        """Init"""
        self.warning_light_on = warning_light_on

    def needs_service(self):
        """Returns true if the car needs service as shown by the warning light"""
        if self.warning_light_on:
            return True
        return False
