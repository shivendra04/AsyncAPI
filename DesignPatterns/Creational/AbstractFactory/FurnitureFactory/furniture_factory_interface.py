from abc import ABCMeta, abstractmethod

class IFurnitureFactory(metaclass=ABCMeta):
    '''abstract furniture factory interface'''

    @staticmethod
    @abstractmethod
    def get_furniture():
        pass