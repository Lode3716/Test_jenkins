"""
   
 auth : l.devigne

"""
import traceback


def div(a, b):
    return a / b


def call_div(a, b):
    try:
        print("Ouverture du fichier ")
        r = div(a, b)
    finally:
        print("Fermeture du fichier ")

    return r


def main():
    a = 0
    b = 2
    try:
        # c = b / a
        c = call_div(b, a)
        print(c)
    except ZeroDivisionError as err:
        print(err)
        traceback.print_exc()
    # finally:
    #     print("Finally")
    else:
        print("Pas d'erreur")

    print("après")


if __name__ == '__main__':
    main()
