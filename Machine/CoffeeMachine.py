from Machine.VendingMachine import VendingMachine
from Product.Coffee import Coffee
import zope.interface 


class CoffeeMachine:
	zope.interface.implementer(VendingMachine)

	def __init__(self):
		self.__coffe_list = []

	def get_products(self):
		for coffee in self.__coffe_list:
			print(f"Name: {coffee.get_name()}\nVolume: {coffee.get_volume()}\n")

	def get_product(self, name: str, volume: int):
		for coffee in self.__coffe_list:
				if coffee.get_name() == name:
					if coffee.get_volume() >= volume:
						coffee.set_volume() = coffee.get_volume() - volume

	def add_products(self, coffee: Coffee):
		if coffee not in self.__coffe_list:
			self.__coffe_list.append(coffee)
