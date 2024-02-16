"""
   
 auth : l.devigne

"""
from builtins import map


def main():
    l1 = [10, 20, 30]
    # retour_list = add(*l1)
    # print(retour_list)

    # print(add(10, 20, 30))
    # l2 = [10, 20, 30, 40, 50]
    # a, b, c, *d = l2
    # print(a, b, c)
    # print(d)
    # print(*l2)

    print(mult_2(*l1))
    print(list(map(mult_3, l1)))  # renvoie l'adresse de l'iterrable, obligé de le caster pour avoir les valeurs
    print(list(map(lambda v: v * 2, l1))) #Avec une lambda en fonction


def add(*ajout_list) -> int:
    retour = 0
    for let in ajout_list:
        retour += let

    return retour


def mult_2(*ajout_list):
    retour = []
    for let in ajout_list:
        retour.append(let * 2)

    return retour


def mult_3(v):
    return v * 2


if __name__ == '__main__':
    main()
