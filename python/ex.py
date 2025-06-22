# дан массив [1,2,3,4,5], есть апи - https://example
# нужно асинхронно опросить апи с заданной параллельностью
# таски/футуры


import asyncio
import aiohttp


ids = range(10)
url = " http://127.0.0.1:8000"
semaphore = asyncio.Semaphore(5)

async def get_data(url: str) -> dict:
    async with semaphore:
        print(f"start {url}")

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data  = await resp.json()
                print(f"finish {url}")
                return data




async def main(ids: list[int], url: str):
    tasks = [asyncio.create_task(get_data(f"{url}/data/{i}")) for i in ids]
    results = await asyncio.gather(*tasks)

    for res in results:
        print(res)





asyncio.run(main(ids, url))
