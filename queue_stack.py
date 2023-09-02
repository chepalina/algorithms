"""
Очередь на стеках. 

Очередь
Добавить элемент в конец очереди
Удалить элемент из начала очереди
Узнавать первый/последний элементы
Сделать таких операций за O(n)
Можно реализовать, используя массив и указатель на начало очереди
лишняя память
capacity n
n + + +. . . +1 ≤ 2n = O(n)
n
2
n
4
n O(n)
C C
n O(n)
n O(n)
Очередь
Можно реализовать, используя 2 стека, представить как два стакана, которые касаются донышками
При добавлении элемента кладем его в правый стек
При удалении удаляем из левого
Если в левом пусто, перекладываем туда по одному все элементы из правого. Они развернутся.
Каждый элемент переложится только 1 раз асимптотика
Пример: ][ ][A ][AB ][ABC ABC][ BC][ BC][D
⇒ O(n)
"""

from typing import Any


class QueueStack:
    def __init__(self):
        self._stack = []  # для добавления элементов
        self._reverse_stack = []  # для извлечения элементов

    def add(self, element: Any):
        self._stack.append(element)

    def pop(self) -> Any:

        if not self._reverse_stack and self._stack:
            self._stack.reverse()
            self._reverse_stack.extend(self._stack)
            self._stack = []

        if self._reverse_stack:
            return self._reverse_stack.pop()
        else:
            raise IndexError("Empty queue")

    def len(self) -> int:
        return len(self._stack) + len(self._reverse_stack)


q = QueueStack()

q.add(5)
q.add(6)

print(q.pop(), q.pop())

q.add(7)
print(q.pop())
