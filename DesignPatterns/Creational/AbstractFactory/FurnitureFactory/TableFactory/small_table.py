from .table_interface import ITable

class SmallTable(ITable):

    def __init__(self):
        self.height = 10
        self.width = 10
        self.length = 10

    def get_dimentions(self):
        return {
            "height":self.height,
            "width":self.width,
            "length":self.length
        }