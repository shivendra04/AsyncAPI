from abc import ABCMeta, abstractmethod

class IChair(metaclass=ABCMeta):
    '''The chair interface (product)'''

    @staticmethod
    @abstractmethod
    def get_dimentions():
        pass
