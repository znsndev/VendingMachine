from zope.interface import Interface


class QueueBehavoir(Interface):
	def accept_to_market(actor: Actor):
		pass
	
	def release_form_market(actors: list):
		pass

	def update():
		pass