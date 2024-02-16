"""
   
 auth : l.devigne

"""

from Cercle import Cercle
from ICalcGeo import ICalcGeo
from Rectangle1 import Rectangle


def show_surface(o: ICalcGeo):
    print(o.surface)


def main():
    ce = Cercle(2)
    re = Rectangle(2, 5)
    print(ce.surface)
    print(re.surface)
    show_surface(ce)
    show_surface(re)


if __name__ == '__main__':
    main()
