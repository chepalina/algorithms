# дан массив [1,2,3,4,5], есть апи - https://example
# нужно асинхронно опросить апи с заданной параллельностью
# таски/футуры

input_list = range(10)
base_url = 'https://test/'

import aiohttp
import asyncio


from aiohttp.client_exceptions import ClientConnectorError


async def get_data(id: int) -> str:
    example_url = f"{base_url}{id}"
    print(f"start {id}")

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(example_url, timeout=1) as resp:
                return resp.text()
    except (ClientConnectorError, asyncio.exceptions.TimeoutError, asyncio.exceptions.CancelledError):
        return example_url

    return str(id)


async def main(input_: list):

    tasks = [asyncio.create_task(get_data(id)) for id in input_]
    results = await asyncio.gather(*tasks)

    # tasks = await asyncio.gather(*(get_data(id) for id in input_))
    print(results)



asyncio.run(main(input_list))

# lock = asyncio.Lock()
# C = 1
#
#
# async def main1():
#     async with lock:
#         global C
#         C += 1


# asyncio.run(main1())
#
# print(C)






