from zope.interface import Interface, Attribute
# from Product.Product import Product


class VendingMachine(Interface):
	def get_products():
		pass

	def get_product():
		pass

	def add_product():
		pass

	def add_products():
		pass