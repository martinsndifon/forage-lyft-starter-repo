from abc import ABC, abstractmethod

class Tyre(ABC):
	"""Base abstract class for tyres"""
	@abstractmethod
	def needs_service(self):
		pass