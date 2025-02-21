from abc import ABCMeta, abstractmethod

class ITable(metaclass = ABCMeta):
    '''table interface'''

    @staticmethod
    @abstractmethod
    def get_dimentions():
        pass