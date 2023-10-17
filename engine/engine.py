from abc import ABC, abstractmethod


class Engine(ABC):
    """Absract base class for the Engines"""
    @abstractmethod
    def needs_service(self):
        pass
