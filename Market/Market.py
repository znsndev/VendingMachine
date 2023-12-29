import zope.interface

from Market.QueueBehavoir import QueueBehavoir 
from Market.MarketBehavoir import MarketBehavoir



class Market:
	zope.interface.implementer(QueueBehavoir, MarketBehavoir)

	def __init__(self, arg):
		self.__queue = []
		self.__orders = []

	def take_in_queue(actor: Actor):
		self.__queue.append(actor)

	def release_from_queue(actor: Actor):
		if actor in self.__queue:
			self.__queue.remove(actor)

	def take_order(self, actor: Actor, order: Product | Bottle | Coffee):
		self.release_from_queue(actor)
		self.__orders.append[order]

	def give_order(self, order: Product | Bottle | Coffee):
		if order in self.__orders:
			self.__orders.remove()

