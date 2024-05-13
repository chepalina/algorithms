# 8 задач
# Задача A. Минимум на стеке

from typing import Optional
from collections import namedtuple

data_tuple = namedtuple("Data", "data min")


class StackMin:
    def __init__(self):
        self._data = []
        self._min = None

    def add(self, value: int):
        data = data_tuple(value, self._min)
        self._data.append(data)
        self._min = value if self._min is None else min(value, self._min)

    def remove(self):
        _, prev_min = self._data.pop()
        self._min = prev_min

    def min(self):
        return self._min


def operate(code: int, stack: StackMin, value: Optional[str]):

    if code == 1:
        stack.add(int(value))
    elif code == 2:
        stack.remove()
    elif code == 3:
        print(stack.min())


# stack = StackMin()
# operations_num = input()
#
#
# for _ in range(int(operations_num)):
#     input_value = input()
#     op, value = input_value.split() if len(input_value) > 1 else (input_value, None)
#     operate(int(op), stack, value)

# Задача B. Минимум на отрезке


from collections import deque


def sliding_window_minimum(arr, k):
    # Инициализация deque и результатов
    deq = deque()
    mins = []

    for i in range(len(arr)):
        if (len(deq) > 0) and (deq[0] <= i - k):
            deq.popleft()  # слишком старый индекс
        while len(deq) > 0 and arr[deq[-1]] >= arr[i]:
            deq.pop()
            # удалить элементы, у которых уже нет шансов стать минимумом в окошке

        deq.append(i)

        if i >= k - 1:
            mins.append(arr[deq[0]])  # голова дека - минимум в текущем окне

    return mins


# Пример массива и размер окна
#
# array = [1, 3, 2, 4, 5, 3, 1]
# k = 3
# # [1, 2, 2, 3, 1]
# print(sliding_window_minimum(array, k))


# Задача C. Постфиксная запись

s = "8 9 + 1 7 - *"
res = -102


def calculate_postfix(input_: str):

    op_catalog = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
    }
    arr = input_.split(" ")
    stack = []

    for el in arr:
        if el not in op_catalog:
            stack.append(int(el))
        else:
            second, first = stack.pop(), stack.pop()
            stack.append(op_catalog.get(el)(first, second))

    return stack[0]


print(calculate_postfix(s))


def count_balls(input_: list) -> int:
    result = 0
    counter = 0
    stack = []
    prev = None

    for i in input_:

        if i != prev:

            if counter < 3:
                stack.append((prev, counter))
                counter = 1
            else:
                result += counter
                prev, counter = stack.pop()

                if prev != i:
                    return result

        if i == prev:
            counter += 1

        prev = i

    if counter > 3:
        result += counter

    return result


#
# print(count_balls([3,3,2,1,1,1,2,2,3,3]))
# assert count_balls([1,3,3,3,2]) == 3
# assert count_balls([3,3,2,1,1,1,2,2,3,3]) == 10
# assert count_balls([3,3,3,3]) == 4


def sort_carriage(carriage: list):
    def check_result(result, prev_op, op):
        prev, count = prev_op

        if prev == op:
            count += 1
            prev_op = (op, count)
        else:
            result.append(prev_op)
            prev_op = (op, 1)

        return result, prev_op

    carriage = carriage[::-1]
    result = []
    dead_end = []
    next_value = 1
    prev_op = (1, 0)

    while carriage or (dead_end and dead_end[-1] == next_value):

        if dead_end and dead_end[-1] == next_value:
            dead_end.pop()
            next_value += 1

            result, prev_op = check_result(result, prev_op, 2)

        else:
            dead_end.append(carriage.pop())

            result, prev_op = check_result(result, prev_op, 1)

    result.append(prev_op)

    return None if carriage or dead_end else result


#
# print(sort_carriage([3, 2, 1]))
# assert sort_carriage([3, 2, 1]) == [(1, 3), (2, 3)]
# assert sort_carriage([4, 1, 3, 2]) == [(1, 2), (2, 1), (1, 2), (2, 3)]
# assert sort_carriage([3, 1, 4, 2]) is None


class Item:
    def __init__(self, id, next, prev):
        self.id = id
        self.next = next
        self.prev = prev


class Queue:
    def __init__(self):
        self._head = None
        self._tail = None

    def __repr__(self):
        return f"H: {self._head.id if self._head else None}, T: {self._tail.id if self._tail else None}"

    def add(self, id: int):
        item = Item(id, None, self._tail)

        if self._head is None:
            self._head = item
        elif self._tail is not None:
            self._tail.next = item

        self._tail = item

    def buy_ticket(self):
        self._head = self._head.next

        if self._head is None:
            self._tail = None

    def leave(self):
        self._tail = self._tail.prev

        if self._tail is None:
            self._head = None
        else:
            self._tail.next = None

    def count(self, id):

        if self._head is None:
            return 0

        counter = 0
        _temp = self._head

        while _temp.id != id:
            counter += 1
            _temp = _temp.next

        return counter

    def get_first(self):
        return self._head.id


def main():
    operations = [(1, 1), (5, 0), (1, 3), (3, 0), (2, 0), (1, 2), (4, 2)]
    q = Queue()

    for op in operations:
        op_num, value = op
        if op_num == 1:
            q.add(value)
            print(q)
        elif op_num == 2:
            q.buy_ticket()
            print(q)
        elif op_num == 3:
            q.leave()
            print(q)
        elif op_num == 4:
            print(q.count(value))
        elif op_num == 5:
            print(q.get_first())


# main()

# Гоблины и очереди ------------------------------------------------------


class ItemG:
    def __init__(self, id, next, prev):
        self.id = id
        self.next = next
        self.prev = prev


class GoblinQueue:

    def __init__(self):
        self._head = None
        self._tail = None

    def add_tail(self, id: int):
        item = ItemG(id, None, self._tail)

        if self._head is None:
            self._head = item
        elif self._tail is not None:
            self._tail.next = item

        self._tail = item

    def add_head(self,id: int):
        item = ItemG(id, self._head, None)

        if self._tail is None:
            self._tail = item
        if self._head is not None:
            self._head.prev = item

        self._head = item

    def get_first(self):
        item = self._head
        self._head = self._head.next

        if self._head is None:
            self._tail = None

        return item.id





class PrivilegeQueue:

    def __init__(self):
        self._first_queue = GoblinQueue()
        self._second_queue = GoblinQueue()
        self._first_count = 0
        self._second_count = 0

    def add(self, id: int):
        self._second_queue.add_tail(id)
        self._second_count += 1
        self._balance()

    def get_first(self):
        id = self._first_queue.get_first()
        self._first_count -= 1
        self._balance()
        return id

    def add_privilege(self, id:int):
        if self._first_count == self._second_count:
            self._first_queue.add_tail(id)
            self._first_count += 1
        else:
            self._second_queue.add_head(id)
            self._second_count += 1

    def _balance(self):
        if self._second_count > self._first_count:
            id = self._second_queue.get_first()
            self._first_queue.add_tail(id)
            self._second_count -= 1
            self._first_count += 1



def main2():

    queue = PrivilegeQueue()
    queue.add(1)
    queue.add(2)
    # print(queue.get_first())
    queue.add(3)
    queue.add(4)

    queue.add_privilege(5)
    print(queue.get_first())
    print(queue.get_first())
    print(queue.get_first())
    print(queue.get_first())
    print(queue.get_first())


# main2()

# Задача H. Хорошие дни-------------------------


def max_sum_times_min(nums):
    n = len(nums)

    # Ближайший меньший слева
    left = [-1] * n

    # Вычисление ближайшего меньшего элемента слева для каждого элемента.
    # Это делается с помощью стека.
    # В стеке будем хранить индексы элементов массива таким образом, чтобы элементы,
    # на которые они указывают, формировали убывающую последовательность.
    # Для каждого нового элемента массива мы будем удалять из стека элементы,
    # пока вершина стека не будет указывать на элемент меньше текущего.
    # Таким образом, вершина стека всегда будет указывать на ближайший меньший элемент слева.
    stack = []
    for i in range(n-1, -1, -1):
        while stack and nums[stack[-1]] > nums[i]:
            left[stack.pop()] = i
        stack.append(i)

    print("left = ", left)

    # Ближайший меньший справа
    right = [n] * n

    # Нахождение для каждого элемента максимально длинного подотрезка,
    # где этот элемент является минимумом.
    # С помощью аналогичного стека, но теперь пройдясь по массиву справа налево,
    # можно найти ближайший меньший элемент справа для каждого элемента.
    # Зная ближайшие меньшие элементы слева и справа для каждого элемента,
    # можно определить для каждого элемента длину максимального подотрезка,
    # на котором он является минимумом.

    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            right[stack.pop()] = i
        stack.append(i)

    print(right)

    # Вычисление префиксных сумм
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i-1] + nums[i-1]

    print(prefix_sum)

    # Поиск максимальной суммы, умноженной на минимум
    max_product = 0
    for i in range(n):
        # Вычисляем сумму подотрезка
        total_sum = prefix_sum[right[i]] - prefix_sum[left[i] + 1]
        mul = total_sum * nums[i]
        # Обновляем максимум, если нужно
        max_product = max(max_product, mul)

    print(max_product)
    return max_product


#
# assert max_sum_times_min([3,1,6,4,5,2]) == 60
# assert max_sum_times_min([1,2,1,2]) == 6


# --------------------------------------------------------
# У вас есть гистограмма - набор прямоугольников шириной 1
#  и высотой N
# , идущих слева направо вплотную, причем они все "стоят" на земле - их нижняя координата y
#  равна 0
# . Задача - найти наибольший по площади прямоугольник, лежащий внутри такой клеточной гистограммы.

l = [1,4,3,5,4,1]


def gist(heights: list) -> int:

    # Добавляем в конец массива высот высоту 0 для упрощения логики обработки конца массива
    heights.append(0)
    stack = [-1]  # Инициализация стека фиктивным индексом
    max_area = 0
    for i, h in enumerate(heights):
        while heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area


print(gist([5, 5,1]))




l2 = [5, 5, 1]


def gist2(heights: list) -> int:

    stack = [(0, -1)]
    heights.append(0)
    max_ans = 0

    for i, h in enumerate(heights):
        while stack[-1][0] > h:

            s_h, s_i = stack.pop()
            height = s_h
            width = i - stack[-1][1] - 1
            max_ans = max(max_ans, height*width)

        stack.append((h, i))

    return max_ans



print(gist2(l2))









l2 = [5, 5, 1]
l3 = [5, 3, 5, 1]
# граница для 5  - по ширине от 3 (индекс 1) до левой границы - индекс -1











