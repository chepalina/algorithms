"""
Cортировка выбором.

Идея: мы можем раз выбрать минимум и составить отсортированный массив
Поиск минимума выполняется в зависимости от размера массива:
На первом шаге минимум надо выбрать из элементов и поставить его на позицию 1
На втором шаге из и поставить его на позицию 2
[5,6,2,3] [2,6,5,3] [2,3,5,6] [2,3,5,6] [2,3,5,6]
"""


input = [5, 6, 2, 3]


def sort(list_to_sort):

    min_index = 0

    for i in range(len(list_to_sort)):
        current_index = i
        current_value = list_to_sort[i]
        min_element = current_value

        for num, j in enumerate(list_to_sort):
            if num < current_index:
                continue
            if num == current_index:
                min_index = current_index

            if j < min_element:
                min_index = num
                min_element = j

        if min_index > current_index:
            list_to_sort[current_index] = min_element
            list_to_sort[min_index] = current_value

    return list_to_sort


print("Cортировка выбором 1. ", sort(input))


input = [5, 6, 2, 3]

input_len = len(input)
unsorted_index = 0

while unsorted_index < input_len:

    min_index = unsorted_index
    for i in range(unsorted_index, input_len):
        if input[i] < input[min_index]:
            min_index = i
    input[unsorted_index], input[min_index] = input[min_index], input[unsorted_index]
    unsorted_index += 1

print("Cортировка выбором 2. ", input)


"""
a = [5,6,2,3]

n = len(a)
k = n - 1

while k >= 1:
    i_max = 0
    for i in range (1 , k + 1) :
        if a[ i] > a[ i_max ]:
            i_max = i
    a[k ], a[ i_max ] = a [ i_max ], a[ k]
    k -= 1


print (a)
"""


"""
Сортировка вставками.

Идея: двигаем элемент влево, пока он не встанет на свое место
Представим, что у нас слева есть отсортированный участок, пусть его длина :
Возьмем -й элемент
Будем двигать его, пока он не встанет на своё место
Получили отсортированный участок размера
[5,6,2,3] [5,6,2,3] [5,6,2,3] [2,5,6,3] [2,3,5,6]
"""

input = [5, 6, 2, 3]
sorted_index = 1

while sorted_index < len(input):
    for i in range(sorted_index, 0, -1):
        if input[i] < input[i - 1]:
            input[i], input[i - 1] = input[i - 1], input[i]

        # оптимизация, для раннего выхода
        if input[i] > input[i - 1]:
            continue

    sorted_index += 1


print("Сортировка вставками. ", input)


"""
Сортировка пузырьком.

Каждый раз будем смещать самый "тяжелый" элемент в конец
Для всех от i 1 до n - 1, если ai > ai+1 обмениваем их местами
Для одного элемента в худшем случае обменов n
Для n элементов n2
Асимптотика O(n2)
Можно понять, что после шага i последние i элементов отсортированы
Пример одного прохода: [5,3,6,2] [3,5,6,2] [3,5,6,2] [3,5,2,6]"""


input = [5, 6, 2, 3]
current_itaration = 0

while current_itaration < len(input):
    for i in range(0, len(input) - 1 - current_itaration):
        if input[i] > input[i + 1]:
            input[i], input[i + 1] = input[i + 1], input[i]

    current_itaration += 1


print("Сортировка пузырьком. ", input)
