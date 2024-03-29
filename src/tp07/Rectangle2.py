"""
   
 auth : l.devigne

"""


class RectangleSingleton:
    """
    La class Rectangle
    """

    __cpt = 0  # variable statique
    __instance = None

    def __init__(self, longueur: int = 0, largeur: int = 0):
        self.__longueur = longueur
        self.__largeur = largeur
        RectangleSingleton.__cpt += 1

    @classmethod
    def buildFromStr(cls, value):
        longueur, largeur = [int(i) for i in value.split('x')]
        return cls(longueur, largeur)

    @staticmethod
    def cpt():
        return RectangleSingleton.__cpt

    @property
    def longueur(self):
        return self.__longueur

    @property
    def largeur(self):
        return self.__largeur

    @longueur.setter
    def longueur(self, longueur):
        self.__longueur = longueur

    @largeur.setter
    def largeur(self, largeur):
        self.__largeur = largeur

    @property
    def surface(self):
        return self.__longueur * self.__largeur

    def __str__(self) -> str:
        return f"{__class__.__name__} {self.__longueur=},{self.__largeur=}"

    def __eq__(self, __value) -> bool:
        return self.longueur == __value.longueur and self.largeur == __value.largeur

    def __new__(cls, *args, **kargs):
        """méthode de construction standard en Python"""
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance
