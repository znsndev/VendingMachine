from Product.Product import Product


class Bottle(Product):
	__volume: float

	def __init__(self, name: str, price:float, volume: float):
		super().__init__(name, price)
		self.__volume = volume

	def __str__(self):
		return super().__str__() + f"Volume: {self.__volume}\n"