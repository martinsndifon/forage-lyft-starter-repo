from abc import ABC, abstractmethod


class Battery(ABC):
    """Absract base class for the Battries"""
    @abstractmethod
    def needs_service(self):
        pass
