"""
   
 auth : l.devigne

"""


def main():
    for i in range(10):
        print(i)
        if i == 5:
            print("OK")
            break

    else:  # s'excute s'il ne trouve pas la valeur
        print("Pas trouvé")




if __name__ == '__main__':
    main()
