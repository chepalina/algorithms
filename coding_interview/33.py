from typing import Any


# 3.3


class EmptyStackError(Exception):
    pass


class SetOfStack:
    def __init__(self, capacity: int):
        self._stack_storage = []
        self._capacity = capacity

    def push(self, value: Any):
        stack = self._create_new() if self.is_empty() else self._get_last()

        if len(stack) == self._capacity:
            stack = self._create_new()

        stack.append(value)

    def pop(self):

        stack = self._get_last()
        element = stack.pop()

        if not stack:
            self._stack_storage.pop()

        return element

    def pop_at(self, number: int):
        stack = self._get_specified(number)
        element = stack.pop()

        if not stack:
            self._stack_storage.remove(number)

        return element

    def is_empty(self) -> bool:
        return not self._stack_storage

    def _create_new(self):
        stack = []
        self._stack_storage.append(stack)
        return stack

    def _get_last(self):
        if self.is_empty():
            raise EmptyStackError()

        return self._stack_storage[-1]

    def _get_specified(self, number: int):
        try:
            return self._stack_storage[number]
        except ValueError as e:
            raise ValueError(f"There are {len(self._stack_storage)} stacks.") from e


s = SetOfStack(3)

s.push(1)
s.push(2)
s.push(3)
s.push(4)

assert s._stack_storage == [[1, 2, 3], [4]]
assert s.pop() == 4
assert s.pop() == 3
assert s.pop() == 2
assert s.pop() == 1

try:
    s.pop()
except EmptyStackError:
    pass
else:
    assert False


# 3.4


class Stack:
    def __init__(self):
        self._stack = []

    def push(self, value: Any):
        self._stack.append(value)

    def pop(self) -> Any:
        if not self._stack:
            raise EmptyStackError()

        return self._stack.pop()

    def is_empty(self) -> bool:
        return not bool(self._stack)


class MyQueue:
    def __init__(self):
        self._newest = Stack()
        self._oldest = Stack()

    def add(self, value: Any):
        self._newest.push(value)

    def remove(self):
        if self.is_empty():
            raise EmptyStackError()

        if self._oldest.is_empty():
            self._reverse()

        return self._oldest.pop()

    def is_empty(self):
        return self._newest.is_empty() and self._oldest.is_empty()

    def _reverse(self):
        while not self._newest.is_empty():
            self._oldest.push(self._newest.pop())


q = MyQueue()
q.add(1)
q.add(2)
q.add(3)

assert q.remove() == 1

q.add(4)

assert q.remove() == 2
assert q.remove() == 3
assert q.remove() == 4
