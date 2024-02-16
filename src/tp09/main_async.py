"""
   
 auth : l.devigne

"""
import asyncio
import time


async def add(a, b):
    await asyncio.sleep(1)
    return a + b


async def main():
    start = time.perf_counter()
    # print('Hello ...')
    # await asyncio.sleep(10)
    # print('... World!')
    all_sync = [add(2, 3), add(3, 12), add(2, 3), add(3, 12), add(2, 3), add(3, 12)]
    res = await asyncio.gather(*all_sync)
    print(res)
    end = time.perf_counter()

    print(end - start)


if __name__ == '__main__':
    asyncio.run(main())
