"""
   
 auth : l.devigne

"""

# from pprint import pprint

import time

import requests
from bs4 import BeautifulSoup


def main():
    start = time.perf_counter()
    response = requests.get("https://logs.eolem.com/")

    # print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")

    all_a = soup.findAll('a')

    # for a in all_a:
    #     if ".log" in a['href']:
    #         print(a['href'])

    links = [a['href'] for a in all_a if ".log" in a['href']]

    # pprint(links)
    # pprint(all_a)

    for downLoad in links:
        with open(downLoad, "w", encoding="utf-8") as fic:
            save = requests.get(f"https://logs.eolem.com/{downLoad}")
            # soup_fic = BeautifulSoup(save.text, "html.parser")
            fic.write(save.text)

    end = time.perf_counter()

    print(f"time : {end - start :.2f} s")


if __name__ == '__main__':
    main()
