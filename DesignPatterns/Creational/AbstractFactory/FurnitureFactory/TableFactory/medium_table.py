from .table_interface import ITable

class MediumTable(ITable):

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