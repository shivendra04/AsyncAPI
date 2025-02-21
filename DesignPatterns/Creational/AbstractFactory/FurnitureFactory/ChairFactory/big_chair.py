from .chair_interface import IChair

class BigChair(IChair):

    def __init__(self):
        self.lenght = 20
        self.width = 20
        self.height = 20

    def get_dimentions(self):
        return {
            "length":self.lenght,
            "width":self.width,
            "height":self.height
        }