from chair_factory import ChairFactory

small_chair = ChairFactory.get_chair("SmallChair")
print(small_chair.get_dimention())
medium_chair = ChairFactory.get_chair("MediumChair")
print(medium_chair.get_dimention())
big_chair = ChairFactory.get_chair("BigChair")
print(big_chair.get_dimention())