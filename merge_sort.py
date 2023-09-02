"""
Сортировка слиянием.

"Разделяй и властвуй"
Делим массив пополам на две части: левую и правую
Допустим, мы их как-то отсортировали
Можем объединить за O(n): идём и выбираем минимальный элемент из двух массивов
Применяем эту идею рекурсивно, пока размер массива больше 1
На каждом "уровне" делаем O(n) операций
Уровней рекурсии ⌈log2 n⌉, потому что каждый раз делим пополам
Итого O(n log n)
"""

x = [3, 6, 1, 10, 2, 7, 9]


# корректный алгоритм со слайсами


def merge_list(left, right):
    print(f"merge {left=}, {right=}")
    left_index = rigtht_index = 0

    merged_list = []
    for _ in range(len(left) + len(right)):
        # print(f"{left_index=}, {rigtht_index=}")

        if left_index == len(left):
            merged_list.append(right[rigtht_index])
            rigtht_index += 1
            continue
        elif rigtht_index == len(right):
            merged_list.append(left[left_index])
            left_index += 1
            continue

        if left[left_index] < right[rigtht_index]:
            merged_list.append(left[left_index])
            left_index += 1
        else:
            merged_list.append(right[rigtht_index])
            rigtht_index += 1

    print(f"sorted list {merged_list}")

    return merged_list


# print(merge_list(left=[5,6,7], right=[1,3,10]))


def sort_3(input_list: list) -> list:
    print(input_list)

    if len(input_list) == 1:
        return input_list

    middle = len(input_list) // 2

    print("call l_sort")
    l = sort_3(input_list[:middle])  # правая половина больше левой
    print("call r_sort")
    r = sort_3(input_list[middle:])

    return merge_list(l, r)


# print(sort_3(x))


# алгоритм на индексах
# алгоритм merge некорректный, нужно ходить кучей проходов, чтобы не затрачивать доп память

x = [1, 4, 10, 2, 8, 15, 200, 3, 7]


def merge(input_list, first_left, first_right, second_left, second_right):
    first_index = first_left
    second_index = second_left

    print(
        f"rigth = {input_list[first_index:first_right+1]} , left = {input_list[second_left:second_right+1]}"
    )

    while first_index <= first_right:
        # print(f"{first_index=}, {first_left=}, {second_index=}, {second_left=}")
        # print(f"{input_list[first_index]=}, {input_list[second_index]=}")
        first_part_element = input_list[first_index]

        if first_part_element < input_list[second_index]:
            first_index += 1
        else:
            for i in range(second_left, second_right + 1):
                if first_part_element > input_list[i]:
                    continue
                else:
                    input_list[first_index], input_list[i - 1] = (
                        input_list[i - 1],
                        input_list[first_index],
                    )
                    first_index += 1
                    break
            else:
                input_list[first_index], input_list[i] = (
                    input_list[i],
                    input_list[first_index],
                )


def sort(input_list: list, left, right) -> list:
    if right == left:
        return

    middle = (right + left) // 2
    # включая значения правой и левой границ
    # print(f"{left=}, {middle=}")
    sort(input_list, left, middle)

    print(f"middle={ middle + 1}, {right=}")
    sort(input_list, middle + 1, right)
    merge(input_list, left, middle, middle + 1, right)


# print("start")
# sort(x, 0, len(x) - 1)
# print(x)


x = [1, 4, 10, 2, 8, 15, 200, 3, 7]

print(x)


def merge(input_list, first_left, first_right, second_left, second_right):

    right = input_list[first_left : first_right + 1]
    left = input_list[second_left : second_right + 1]
    sorted_list = []

    print(f"rigth = {right} , left = {left}")

    while right or left:
        if not right:
            sorted_list.append(left.pop(0))

        elif not left:
            sorted_list.append(right.pop(0))

        elif right[0] < left[0]:
            sorted_list.append(right.pop(0))

        elif left[0] < right[0]:
            sorted_list.append(left.pop(0))

        else:
            raise Exception("Unexpected condition")

    input_list[first_left : second_right + 1] = sorted_list


# merge(x, 0, 2, 3, 4)


def sort(input_list: list, left, right) -> list:
    if right == left:
        return

    middle = (right + left) // 2
    # включая значения правой и левой границ
    # print(f"{left=}, {middle=}")
    sort(input_list, left, middle)

    # print(f"middle={ middle + 1}, {right=}")
    sort(input_list, middle + 1, right)

    merge(input_list, left, middle, middle + 1, right)


print("start")
sort(x, 0, len(x) - 1)
print(x)


"""
Попытки - некорректные алгоритмы. 
"""

# 1 step
def sort(input_list: list, left, right) -> list:
    print(input_list)

    if len(input_list) == 1:
        return input_list
    if not input_list:
        raise Exception("shit")

    middle = (left + right) // 2

    print(f"{left=}, {right=}, {middle=}")

    l = input_list[left:middle]  # левая половина больше правой
    r = input_list[middle : right + 1]

    print(f"{l=}, {r=}")

    # мерж списков некорректный
    for i in range(left, middle):

        if i + middle < len(input_list) and input_list[i] > input_list[i + middle]:
            print("changing... ", input_list[i], " and ", input_list[i + middle])

            input_list[i], input_list[i + middle] = (
                input_list[i + middle],
                input_list[i],
            )

    return input_list


def sort_2(input_list: list, left, right) -> list:
    print(input_list[left : right + 1])

    if len(input_list) == 1:
        return input_list
    # if not input_list:
    #     raise Exception("shit")

    middle = (left + right) // 2

    print(f"{left=}, {right=}, {middle=}")

    print("call l_sort")
    l = sort_2(input_list, left, middle - 1)  # правая половина больше левой
    print("call r_sort")
    r = sort_2(input_list, middle, right)

    print(f"{l=}, {r=}")

    # мерж списков некорректный
    for i in range(left, middle):

        if i + middle < len(input_list) and input_list[i] > input_list[i + middle]:
            print("changing... ", input_list[i], " and ", input_list[i + middle])

            input_list[i], input_list[i + middle] = (
                input_list[i + middle],
                input_list[i],
            )

    return input_list


# print(sort_2(x, 0, len(x) - 1))
