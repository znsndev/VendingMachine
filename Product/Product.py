class Product:
	__name: str
	__price: float

	def __init__(self, name: str, price: float):
		self.__name = name
		self.__price = price

	def __str__(self):
		return f"Name: {self.__name}\nPrice: {self.__price}\n"



	def set_name(self, new_name: str):
		self.__name = new_name

	def get_name(self) -> str:
		return self.__name


	def set_price(self, new_price: float):
		if new_price > 0:
			self.__price = new_price

	def get_price(self) -> float:
		return self.__price

