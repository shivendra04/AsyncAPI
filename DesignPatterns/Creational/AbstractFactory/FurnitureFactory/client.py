from furniture_factory import FurnitureFactory

small_chair = FurnitureFactory.get_furniture("SmallChair")

print(small_chair.get_dimentions())

big_table = FurnitureFactory.get_furniture("BigTable")

print(big_table.get_dimentions())