from abc import ABC, abstractmethod


class Serviceable:
    """Abstract base class for serviceable cars"""
    @abstractmethod
    def needs_service(self):
        pass
