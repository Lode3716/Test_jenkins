"""
   
 auth : l.devigne

"""


class A:
    def __init__(self) -> None:
        print('__init__ A')

    def show(self):
        print("A")


class B(A):
    def __init__(self) -> None:
        super().__init__()
        print('__init__ B')

    def show(self):
        print("B")


class C(A):
    def __init__(self) -> None:
        super().__init__()
        print('__init__ C')

    def show(self):
        print("C")


class D(B, C):
    def __init__(self) -> None:
        super().__init__()
        print('__init__ D')

    def show(self):
        # super().show()
        super(B, self).show()
        super(C, self).show()
        print("D")


def main():
    d = D()
    print(D.mro())
    d.show()


if __name__ == '__main__':
    main()
