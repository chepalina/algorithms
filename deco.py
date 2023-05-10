from typing import Callable
from functools import wraps


def deco_params(a):
    def deco(fn: Callable):
        @wraps(fn)
        def inner(*args, **kwargs):
            print(f"Inner decorator {a}")
            return fn(*args, **kwargs)
        return inner
    return deco



class Decorator:

    def __init__(self, a):
        self.a = a

    def __call__(self, fn):
        def inner(*args, **kwargs):
            print(f"Inner decorator {self.a}")
            return fn(*args, **kwargs)
        return inner



@Decorator(1)
def a():
    pass









a()



