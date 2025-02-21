from interface_chair import IChair

class BigChair(IChair):

    def __init__(self):
        self.depth = 20
        self.height = 20
        self.width = 20

    def get_dimention(self):
        return {
            "height":self.height,
            "width":self.width,
            "depth":self.depth
        }