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


# 3.5
from collections import namedtuple


class Stack35:

    Node = namedtuple("Node", "value next")

    def __init__(self):
        self._top = None

    def pop(self):
        if self.is_empty():
            raise EmptyStackError()

        element = self._top.value
        self._top = self._top.next
        return element

    def push(self, value):
        self._top = self.Node(value=value, next=self._top)

    def peek(self):
        if self.is_empty():
            raise EmptyStackError()

        return self._top.value

    def is_empty(self):
        return self._top is None


class SortStack:

    def __init__(self):
        self.primary = Stack35()
        self.secondary = Stack35()

    def push(self, value):
        self.primary.push(value)

    def pop(self):
        if self.is_empty():
            raise EmptyStackError()

        if self.primary is not None:
            self._sort()

        return self.secondary.pop()

    def peek(self):
        pass

    def is_empty(self):
        return self.primary.is_empty() and self.secondary.is_empty()

    def _sort(self):
        while not self.primary.is_empty():
            temp = self.primary.pop()

            while not self.secondary.is_empty() and self.secondary.peek() > temp:
                self.primary.push(self.secondary.pop())

            self.secondary.push(temp)


s = SortStack()
s.push(1)
s.push(10)
s.push(5)
s.push(6)
s.push(2)


assert s.pop() == 10
assert s.pop() == 6


# 3.6

# queue_node = namedtuple("QueueNode", "data next")
from dataclasses import dataclass
from typing import Optional


@dataclass()
class Animal:
    name: str
    order: Optional[int] = None

    def is_older(self, animal: "Animal"):
        if self.order is None:
            raise ValueError()

        return self.order < animal.order


@dataclass()
class Cat(Animal):
    pass


@dataclass()
class Dog(Animal):
    pass


@dataclass()
class QueueNode:
    data: Any
    next: Optional["QueueNode"] = None


class MyQueue:

    def __init__(self):
        self.first = None
        self.last = None

    def add(self, item):
        node = QueueNode(data=item, next=None)

        if self.is_empty():
            self.first = node
        else:
            self.last.next = node

        self.last = node

    def remove(self):
        if self.is_empty():
            raise EmptyStackError()

        data = self.first.data
        self.first = self.first.next

        if self.first is None:
            self.last = None

        return data

    def peek(self):
        if self.is_empty():
            raise EmptyStackError()
        return self.first.data

    def is_empty(self):
        return self.first is None


CAT_TYPE = "CAT"
DOG_TYPE = "DOG"


class AnimalShelter:

    def __init__(self):
        self._cats = MyQueue()
        self._dogs = MyQueue()
        self._counter = 0

    def enqueue(self, animal: Animal):
        self._counter += 1
        animal.order = self._counter

        if isinstance(animal, Cat):
            self._cats.add(animal)
        elif isinstance(animal, Dog):
            self._dogs.add(animal)
        else:
            raise ValueError()

    def dequeue_any(self):
        if self._cats.is_empty() and self._dogs.is_empty():
            raise EmptyStackError()

        if self._cats.is_empty():
            return self.dequeue_dog()

        if self._dogs.is_empty():
            return self.dequeue_cat()

        cat = self._cats.peek()
        dog = self._dogs.peek()

        return self.dequeue_cat() if cat.is_older(dog) else self.dequeue_dog()

    def dequeue_cat(self):
        return self._cats.remove()

    def dequeue_dog(self):
        return self._dogs.remove()


s = AnimalShelter()

s.enqueue(Cat("Barsik"))
s.enqueue(Cat("Murka"))
s.enqueue(Dog("Bobik"))
s.enqueue(Cat("Ryzhik"))
s.enqueue(Dog("Bezzubik"))


assert s.dequeue_dog() == Dog("Bobik", 3)
assert s.dequeue_any() == Cat("Barsik", 1)
assert s.dequeue_any() == Cat("Murka",2)
assert s.dequeue_any() == Cat("Ryzhik", 4)
assert s.dequeue_dog() == Dog("Bezzubik",5)
assert s._cats.is_empty()
assert s._dogs.is_empty()


s.enqueue(Cat("Murka"))
s.enqueue(Dog("Bobik"))

assert s.dequeue_any() == Cat("Murka",6)
assert s.dequeue_any() == Dog("Bobik", 7)
