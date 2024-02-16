"""
   
 auth : l.devigne

"""
import copy


def main():
    l = [10, 20, 30, 40, 50]
    print(l[1:4])

    print(l[-1])  # dernier élément

    print(l[:3])  # premiers éléments de la liste

    print(l[3:])  # du 3eme à la fin

    l1 = l[:]  # l.copy copie des valeurs de la liste
    l[0] = 1000
    print(l)
    print(l1)

    l2 = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]

    print(l2)

    l3 = l2.copy()  # copie superficielle nous reécupérons la référence : shadowcopy
    l4 = copy.deepcopy(l2)  # copie complète toutes les valeurs : deepcopy
    l2[1][1] = 1000

    print(l3)
    print(l4)

if __name__ == '__main__':
    main()
