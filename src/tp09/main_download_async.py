import asyncio
import os
import time

import aiohttp
import httpx
import requests
from bs4 import BeautifulSoup


async def download_old(link):
    loop = asyncio.get_event_loop()
    log_file = link.split('/')[-1]
    download_dir = "./logs"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    response = await loop.run_in_executor(None, requests.get, link)
    with open(f"{download_dir}/{log_file}", "w") as f:
        f.write(response.text)


async def download_aiohttp(link):
    log_file = link.split('/')[-1]
    download_dir = "./logs"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            with open(f"{download_dir}/{log_file}", "w") as f:
                f.write(await response.text())


async def download_httpx(link):
    log_file = link.split('/')[-1]
    download_dir = "./logs"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    async with httpx.AsyncClient() as client:
        response = await client.get(link)

    with open(f"{download_dir}/{log_file}", "w") as f:
        f.write(response.text)


async def main():
    start = time.perf_counter()
    root_url = "https://logs.eolem.com"
    response = requests.get(root_url)

    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = soup.find_all('a')

    links = [a['href'] for a in all_a if ".log" in a['href']]

    tasks = []
    for link in links:
        url = f"{root_url}/{link}"
        tasks.append(download_aiohttp(url))

    await asyncio.gather(*tasks)
    end = time.perf_counter()

    print(f"time : {end - start:.2f} s")


if __name__ == '__main__':
    asyncio.run(main())
