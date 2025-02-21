from .table_interface import ITable

class BigTable(ITable):

    def __init__(self):
        self.length = 20
        self.width = 20
        self.height = 20

    def get_dimentions(self):
        return {
            "length":self.length,
            "width":self.width,
            "height":self.height
        }