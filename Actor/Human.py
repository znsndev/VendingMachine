import zope.interface

from Actor.ActorBehavoir import ActorBehavoir
from Actor.Actor import Actor

class Human(Actor):
	zope.interface.implementer(ActorBehavoir)

	def __init__(self, name: str):
		self.__name = name
		self.__is_ordered = False


	def get_name(self) -> str:
		return self.__name

	def make_order(self):
		self.__is_ordered = True

	def take_order(self):
		self.__is_ordered = False

	def is_ordered(self) -> bool:
		return self.__is_ordered
