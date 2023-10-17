from tyres.tyre import Tyre


class CarriganTyre(Tyre):
    """Defines the Carrigan tyre"""

    def __init__(self, tyres_wear_arr):
        """Init"""
        self.tyres_wear_arr = tyres_wear_arr

    def needs_service(self):
        """Returns True if the tyre needs to be serviced else false"""
        if any(num >= 0.9 for num in self.tyres_wear_arr):
            return True
        return False
