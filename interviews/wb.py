#Наиболее
# часто
# встречающиеся
# элементы
# Дан
# массив
# целых
# чисел
# nums
# и
# целое
# число
# k.Нужно
# написать
# функцию, которая
# вынимает
# из
# массива
# k
# наиболее
# часто
# встречающихся
# элементов
# [1, 1, 4, 1, 3, -1, 4]
# k = 1 = > [1]
# k = 2 = > [1, 4]
#
# {1: 3, 4: 2, 3: 1, -1: 1}


def get_firs(nums: list, k: int) -> list:
    counter = {}

    for n in nums:
        count = counter.get(n, 0)
        counter[n] = count + 1

    counter.sort(key=lambda x: counter[x], asc_order=False)

    return [key for key in counter][0:k]


# Написать
# декоратор, который
# логирует
# результат
# выполнения
# функции
# и
# ее
# общее
# время
# выполнения

import logging

logger = logging.get_logger("decorator")

from typing import Callable
from time import proc_counter
from functools import wraps


def timer(func: Callable):
    @wraps(func)
    def inner(*args, **kwargs):
        start = proc_counter()
        try:
            result = func(*args, **kwargs)
            logger.debug(result)
            return result

        finally:
            result_time = proc_counter() - start
            logger.info(f"{func.__name__}: {result_time}")

    return inner


@timer
def a():
    pass

#
# Даны
# 1
# млн
# аргументов
# и
# 3
# сервиса.
# Надо
# с
# каждым
# из
# аргументов
# сделать
# запрос
# к
# 3
# м
# сервисам,
# получить
# ответ
# и
# вывести
# результаты
# в
# сгруппированном
# виде

ARGS = [..., (), ...]
service1 = 1
service2 = 2
service3 = 3

import aiohttp
import asyncio


async def get_data(item: str, url) -> list[dict]:
    url = f"{url}/{item}"

    async with aiohttp.session(url) as session:
        async with session.get(url, timeout=5) as resp:
            data = await resp.json()

    return data


async def manage_service(service: str, args_list: list):
    tasks = (asyncio.create_tasks(get_data(service1, i)) for i in ARGS)

    async with asyncio.limit():
        result = await asyncio.gather(tasks)

    return result


async def main(services: list):
    result_group = []

    async for service in services:
        result_group.append(await manage_service(service, ARGS))

    return result_group


asyncio.run(main([]))









