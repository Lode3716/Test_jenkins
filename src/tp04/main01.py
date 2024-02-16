"""
   
 auth : l.devigne

"""
from DataRectangle import DataRectangle
from Rectangle import Rectangle


def main():
    r = Rectangle(2, 3)
    print(r)
    r1 = Rectangle(2, 3)
    print(r.__eq__(r1))

    print(Rectangle.cpt())
    # print(Rectangle.__cpt)

    r3 = Rectangle.buildFromStr("52x6")
    print(r3.__dict__)

    print(50 * '-')
    dr = DataRectangle(5, 6)
    dr1 = DataRectangle(5, 6)
    if dr == dr1:
        print("OK")
    else:
        print("KO")


if __name__ == '__main__':
    main()
