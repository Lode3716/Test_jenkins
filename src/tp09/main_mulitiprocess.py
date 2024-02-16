"""
   
 auth : l.devigne

"""

import os
import time
from multiprocessing import Pool


def fonc(x):
    start = time.time()
    while time.time() - start < 2:
        pass
    return x * x


def main():
    start = time.perf_counter()
    print(os.cpu_count())

    with Pool(2) as p:
        print(p.map(fonc, range(100)))

    end = time.perf_counter()

    print(f"time : {end - start :.2f} s")


if __name__ == '__main__':
    main()
