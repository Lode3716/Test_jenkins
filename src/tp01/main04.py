"""
   
 auth : l.devigne

"""
from collections import deque


def main():
    l = [10, 20, 30]
    l.append(40)
    print(l)
    last = l.pop()
    print(l)
    print(last)
    l.insert(0, 1000)
    print(l)
    fisrt = l.pop(0)
    print(fisrt)

    d = deque(l) # ajoute appendleft et popleft pour optimisé le temps de réponse le left ets le premier élément de la liste
    d.appendleft(1000)
    print(l)
    print(d)


if __name__ == '__main__':
    main()
