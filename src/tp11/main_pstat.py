"""
   
 auth : l.devigne

"""
import argparse
import pstats
from pstats import SortKey


def main(the_file):
    p = pstats.Stats(the_file)
    # print(p.print_stats())
    p.sort_stats(SortKey.TIME).print_stats(3)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('the_file', help="Hooooo le fichier !!!")
    params = args.parse_args()

    main(params.the_file)
