from interface_chair import IChair

class SmallChair(IChair):
    
    def __init__(self):
        self.height = 10
        self.width = 10
        self.depth = 10
    def get_dimention(self):
        return {
            "height":self.height,
            "width":self.width,
            "depth":self.depth
        }