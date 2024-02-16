"""
   
 auth : l.devigne

"""
from Rectangle2 import RectangleSingleton as rs
from Rectangle3 import Rectangle as rcs


def main():
    re = rs(2, 5)
    re1 = rs(3, 8)
    print(hex(id(re)))
    print(hex(id(re1)))

    print(hex(id(re1)) == hex(id(re)))

    re.largeur = 12
    print(re.largeur)
    print(re1.largeur)
    print(re.largeur)

    print(type(rs))

    re2 = rcs(2, 5)
    re3 = rcs(2, 5)
    print(hex(id(re2)))
    print(hex(id(re3)))
    print(re2.largeur)

    print(hex(id(re3)) == hex(id(re2)))

    re2.largeur = 14
    print(re2.largeur)
    print(re3.largeur)


    print(type(rcs))


if __name__ == '__main__':
    main()
