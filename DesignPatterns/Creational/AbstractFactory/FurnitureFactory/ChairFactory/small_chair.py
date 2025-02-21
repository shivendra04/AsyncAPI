from .chair_interface import IChair

class SmallChair(IChair):
    
    def __init__(self):
        self.height = 10
        self.width = 10
        self.length = 10

    def get_dimentions(self):
        return {
            "height":self.height,
            "width":self.width,
            "lenght":self.length
        }