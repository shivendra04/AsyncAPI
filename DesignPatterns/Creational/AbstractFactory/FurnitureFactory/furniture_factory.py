from furniture_factory_interface import IFurnitureFactory
from ChairFactory.chair_factory import ChairFactory
from TableFactory.table_factory import TableFactory

class FurnitureFactory(IFurnitureFactory):

    @staticmethod
    def get_furniture(furniture):
        if furniture in ["SmallChair", "MediumChair", "BigChair"]:
            return ChairFactory().get_chair(furniture)
        elif furniture in ["SmallTable", "MediumTable", "BigTable"]:
            return TableFactory().get_table(furniture)
        else:
            None