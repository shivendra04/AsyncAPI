from interface_chair import IChair

class MediumChair(IChair):

    def __init__(self):
        self.depth = 15
        self.height = 15
        self.width = 15

    def get_dimention(self):
        return {
            "height":self.height,
            "width":self.width,
            "depth":self.depth
            }