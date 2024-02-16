"""
   
 auth : l.devigne

"""
import math

from tp06.ICalcGeo import ICalcGeo


class Cercle(ICalcGeo):

    def __init__(self, init_rayon=0) -> None:
        self.__rayon = init_rayon

    @property
    def rayon(self):
        return self.__rayon

    @rayon.setter
    def rayon(self, value):
        self.__rayon = value

    @property
    def surface(self):
        return math.pi * pow(self.__rayon, 2)  # ou self.__rayon**2
