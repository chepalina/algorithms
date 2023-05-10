"""A. Кража в магазине
ограничение по времени на тест1 секунда
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
В магазине компьютерной техники ночью произошла кража.

До этого все клавиатуры, которые продавались в магазине, были пронумерованы по очереди, начиная с некоторого натурального числа x
. Например, если x=4
 и в магазине продавалось 3
 клавиатуры, то они имели номера 4
, 5
 и 6
, а если x=10
 и в магазине продавалось 7
 клавиатур, то они имели номера 10
, 11
, 12
, 13
, 14
, 15
 и 16
.

После кражи в магазине осталось n
 клавиатур с номерами a1,a2,…,an
. Определите минимальное количество клавиатур, которые могли быть украдены, если никто из сотрудников магазина не помнит значение x
.

Входные данные
Первая строка содержит одно целое число n
 (1≤n≤1000)
 — количество оставшихся в магазине клавиатур.

Вторая строка содержит n
 различных целых чисел a1,a2,…,an
 (1≤ai≤109)
 — номера клавиатур, оставшихся в магазине после кражи. Все значения ai
 заданы в произвольном порядке и попарно различны.

Выходные данные
Выведите минимальное количество клавиатур, которые могли быть украдены, если никто из сотрудников магазина не помнит значение x
.

Примеры
входные данныеСкопировать
4
10 13 12 8
выходные данныеСкопировать
2
входные данныеСкопировать
5
7 5 6 4 8
выходные данныеСкопировать
0
Примечание
В первом примере, если x=8
, то минимальное количество клавиатур, украденных из магазина, равно 2
. То есть были украдены компьютеры с номерами 9
 и 11
.

Во втором примере, если x=4
, то ни одна клавиатура не была украдена из магазина."""




def count_stolen_items(remainder: int, number_list: list) -> int:
    """Сложность - O(n) + O(n) = O(n)"""

    max_number = max(number_list)
    min_number = min(number_list)
    actual_count = max_number - min_number + 1

    return actual_count - remainder

print(count_stolen_items(4, [10, 13, 12, 8]))
print(count_stolen_items(5, [7, 5, 6, 4, 8]))



"""
Разбор
Обратим внимание, что единственный способ минимизировать предполагаемое число украденных клавиатур - считать, что нумерация клавиатур
начиналась с минимального имеющегося числа в списке и заканчивалась
максимальным.
4
В таком случае нам достаточно отсортировать массив по возрастанию и
найти разность всех соседних элементов:
X
N
i=1
ai - ai-1 - 1
Асимптотика решения: O(N x log N)
Бонус: существует решение за O(N)
Авторское решение
n = int ( input () )
a = list ( map (int , input () . split () ) )
a. sort ()
cnt = 0
for i in range (1 , n ):
cnt += a [i] - a [i - 1] - 1
print ( cnt )
"""