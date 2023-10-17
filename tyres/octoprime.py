from tyres.tyre import Tyre


class OctoprimeTyre(Tyre):
    """Defines the Octoprime tyre"""

    def __init__(self, tyres_wear_arr):
        """Init"""
        self.tyres_wear_arr = tyres_wear_arr

    def needs_service(self):
        """Returns True if the tyre needs to be serviced else false"""
        if sum(self.tyres_wear_arr) >= 3:
            return True
        return False
