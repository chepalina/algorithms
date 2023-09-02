# 1 - 1
# 2 - 2
# 3 - 3
# 4 - 5
# 5 - 8

def fib(n):
    first = 0
    second = 1

    for _ in range(2,n+1):
        res = first + second
        first, second = second, res

    return res


print(fib(10))
assert fib(10) == 55
