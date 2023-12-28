from Product.Product import Product


class HotDrink(Product):
	__temperature: int

	def __init__(self, name: str, price: float, temperature: int):
		super().__init__(name, price)
		self.__temperature = temperature

	def __str__(self):
		return super().__str__() + f"Temperature: {self.__temperature}\n"