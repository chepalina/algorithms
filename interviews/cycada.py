def func(value):
    print(f"Id : {id(value)}")


x = 1

print(id(x))
func(x)



l = [500, 1, 2, 3]

# l.sort()
# print(l[-2])


def find_prev_max(l: list):

    if len(l) < 2:
        return -1

    max_value = -1
    prev_max = -1

    for i in l:

        prev_max = max_value if i > max_value else max(prev_max, i)
        max_value = max(i, max_value)

    return prev_max


print(find_prev_max(l))
