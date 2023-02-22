"""В этой задаче было необходимо реализовать стек при помощи структуры
vector или её аналога в используемом вами языке (list для Python, List<T>
для C#, ArrayList<T> для Java и т.п.).
Особое внимание следовало обратить на формат ответа вашей программы на каждую из команд:
• Команда push требовала вывод ok
• Команда clear требовала вывод ok
• Команда pop требовала вывод удаляемого элемента или сообщения
’error’, если стек пуст
• Команда back требовала вывод сообщения ’error’, если стек пуст"""


from typing import Any

class Stack:

    def __init__(self):
        self._stack: list = []

    def push(self, element: Any):
        self._stack.append(element)

    def clear(self):
        self._stack = []
        print("ok")

    def pop(self) -> Any:
        try: 
            return self._stack.pop()
        except IndexError:
            print("error")
         
    




