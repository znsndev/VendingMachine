from Product.Product import Product


class Coffee(Product):
	__temperature: int
	__volume: float
	__name: str
	__price: float

	def __init__(self, name: str, price: float, volume: float, temperature: int):
		super().__init__(name, price)
		self.__temperature = temperature
		self.__volume = volume

	def __str__(self):
		return super().__str__() + f"Temperature: {self.__temperature}\n"

	def get_volume(self) -> float:
		return self.__volume

	def set_volume(self, new_volume: float):
		self.__volume = new_volume