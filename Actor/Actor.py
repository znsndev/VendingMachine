from abc import ABC, abstractmethod

class Actor(ABC):
	__name: str
	__is_ordered: bool

	@abstractmethod
	def get_name():
		pass
		