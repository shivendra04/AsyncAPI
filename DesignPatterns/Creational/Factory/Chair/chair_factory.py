from small_chair import SmallChair
from big_chair import BigChair
from medium_chair import MediumChair

class ChairFactory:
    "Chair factory class"

    @staticmethod
    def get_chair(chair):
        if chair == "SmallChair":
            return SmallChair()
        elif chair == "BigChair":
            return BigChair()
        elif chair == "MediumChair":
            return MediumChair()
        else:
            print("Not supported shair")