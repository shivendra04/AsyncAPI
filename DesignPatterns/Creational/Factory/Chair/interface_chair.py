from abc import ABCMeta, abstractmethod

class IChair(metaclass = ABCMeta):
    """Chair interface"""

    @staticmethod
    @abstractmethod
    def get_dimention():
        pass