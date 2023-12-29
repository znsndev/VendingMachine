from zope.interface import Interface
from Actor.Actor import Actor


class QueueBehavoir(Interface):
	def take_in_queue(actor: Actor):
		pass

	def release_from_queue():
		pass

	def take_order():
		pass

	def give_order():
			pass
