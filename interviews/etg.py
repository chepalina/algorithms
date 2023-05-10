# # 1. Напиши декоратор функции, который делает retry в случае ошибки. Ошибкой считаем ситуацию, когда декорируемая функция генерирует исключение
#
# # количество ретраев, список исключений, только синхронный
#
#
# import logging
# from functools import wraps
#
#
#
# class RetryDecorator:
#
#     def __init__(self, retry_num: int, exception_list: list):
#         self.retry_num = retry_num
#         self.exception_list = exception_list
#         self.logger = logging.get_logger("RetryDecorator")
#
#
#     def __call__(fn, *args1, **kwargs1):
#
#         @wraps(fn)
#         def inner(*args, **kwargs):
#             for enum, retry in enumerate(retry_num):
#
#                 try:
#                     result = fn(*args, **kwargs)
#                     break
#                 except tuple(exception_list) as ex:
#                     self.logger.info(f"{enum} Retry. Reason {ex}")
#
#
#             else:
#                 raise ex
#
#             return result
#
#         return  inner
#
#
#
# @RetryDecorator(retry_num=2, exception_list=[Exception])
# def a():
#     pass
#
#
#     # 2. У нас есть страница списывания денег с карты. На ней есть итоговая цена и  форма ввода карты
#     #     - Надо спроектировать API для возможности списания денег с карты клиента
#
#
#     # Оплата только картой, ответ - редирект на страницу банка, ответ долгий
#
#
#     Input:
#     card
#     price
#     payment_id
#
# Card:
# number
# cvv
# date
# card_holder
#
# PaymentResult:
# success_flg
# need_3ds_auth
# link_redirect
# message
# status
#
# success = success_flg is True
# 3ds = need_3ds_auth is True
# fail = success_flg is False
#
# POST /cards-validation {Card} -> ValidationResult(valid_flg, message)
#
# POST /payments {Card, price} -> task_payment_id
# GET /payments/{task_payment_id} -> PaymentResult
#
#
#
# availability:
# | hotel_slug  | date       | rooms_count |
# ------------------------------------------
# | ibis_batumi | 2023-03-01 | 2           |
# | ibis_batumi | 2023-03-02 | 1           |
# | ibis_batumi | 2023-03-03 | 2           |
#
# orders:
# | user_id | hotel_slug  | start_date | end_date   |
# ---------------------------------------------------
# | 1       | ibis_batumi | 2023-03-01 | 2023-03-03 |
#
# Пользователь 1 (начал чуть раньше):
# - успешно создаётся ордер
# - количество доступных комнат уменьшается на 1
#
# Пользователь 2:
# - получил сообщение что нет доступных комнат
#
# Напиши функцию create_order(user_id: int, hotel_slug: str, start_date: datetime, end_date: datetime), которая сохраняет зказ в БД, а при отсутсвии свободных комнат сообщает об этом
#
# begin
# select for update rooms_count from availability av where hotel_slug = 'hotel_slug' and av.date between start_date and end_date
# select min(rooms_count) min_rooms_count from availability av where hotel_slug = 'hotel_slug' and av.date between start_date and end_date
# if min_rooms_count >1 :
#     insert into orders (user_id, hotel_slug, start_date, end_date) values()
#
# update availability
# set
# rooms_count = rooms_count - 1
# where hotel_slug = 'hotel_slug' and av.date between start_date and end_date
#
# commit
#
#
#
#
