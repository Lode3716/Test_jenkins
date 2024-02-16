"""
   
 auth : l.devigne

"""


def make_inc(v):
    def do_inc(vi):
        return v + vi

    return do_inc  # on renvoie la fonction, si on  renvoyait do_inc(vi) boucle infini


def main():
    inc = make_inc(12)
    r = inc(5)
    print(r)


if __name__ == '__main__':
    main()
