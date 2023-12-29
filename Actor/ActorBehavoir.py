from zope.interface import Interface

class ActorBehavoir(Interface):
	def set_make_order():
		pass

	def set_take_order():
		pass

	def is_ordered():
		pass
		