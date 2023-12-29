from zope.interface import Interface


class VendingMachine(Interface):
	def get_products():
		pass

	def get_product():
		pass

	def add_product():
		pass

	def add_products():
		pass