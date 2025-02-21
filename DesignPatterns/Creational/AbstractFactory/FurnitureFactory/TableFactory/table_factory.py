from .small_table import SmallTable
from .medium_table import MediumTable
from .big_table import BigTable

class TableFactory:

    @staticmethod
    def get_table(table):
        if table == "SmallTable":
            return SmallTable()
        elif table == "MediumTable":
            return MediumTable()
        elif table == "BigTable":
            return BigTable()
        else:
            return None