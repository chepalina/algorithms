# дан массив [1,2,3,4,5], есть апи - https://example
# нужно асинхронно опросить апи с заданной параллельностью


ids = range(10)
url = "http://127.0.0.1:8000"

import asyncio
import aiohttp


async def get_data(url: str) -> dict:
    print(f"start {url}")

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            print(f"finish {url}")
            return data


async def main(url: str, ids: list[int]):
    # tasks = [asyncio.create_task(get_data(f"{url}/data/{i}")) for i in ids]

    results = []
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(get_data(f"{url}/data/{i}")) for i in ids]

    # results = await asyncio.gather(*[get_data(f"{url}/data/{i}") for i in ids])

    print([t.result() for t in tasks])




asyncio.run(main(url, ids))


import time
from functools import wraps

def time_logger(func):

    @wraps
    def inner(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        print(time.perf_counter() - start)
        return res

    return inner





@time_logger
def a(r=1, n=0):
    print(r+n)

