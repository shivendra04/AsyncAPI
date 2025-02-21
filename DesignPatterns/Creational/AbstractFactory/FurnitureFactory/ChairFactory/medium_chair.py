from .chair_interface import IChair

class MediumChair(IChair):

    def __init__(self):
        self.length = 15
        self.width = 15
        self.height = 15

    def get_dimentions(self):
        return {
            "length":self.length,
            "width":self.width,
            "height":self.height
            }