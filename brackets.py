"""3 C. Правильная скобочная последовательность
Разбор
Давайте поймём, что если мы удалим из правильной скобочной последовательности S сбалансированную пару скобок, например, (), [], {}, то она
останется правильной.
Тогда последовательно удалив все пары сбалансированных скобок из S,
мы гарантированно получим пустую последовательность.
Воспользовавшись этим, давайте будем удалять все найденные сбалансированные пары скобок в порядке обхода строки. Тогда если после обработки всех символов строки у нас ещё остались хоть какие-то скобки, то S
не являлась ПСП."""


brackets = {"{": "}", "(": ")", "[": "]"}


def is_brackets_valid(input_string: str) -> bool:

    stack = []
    for element in input_string:
        if element in brackets.keys():
            stack.append(element)
        elif element in brackets.values():
            pair = stack.pop()

            reverse_pair = brackets.get(pair)
            if element != reverse_pair:
                return False

    return not bool(stack)


print(is_brackets_valid("()()("))

print(is_brackets_valid("()()()"))

print(is_brackets_valid("[(3 + 6)()]"))

print(is_brackets_valid("[(3 + } 6)()]"))


pairs = {")": "(", "]": "[", "}": "{"}


def check(s):

    stack = []
    for c in s:
        stack.append(c)
        if len(stack) > 1 and c in pairs.keys() and stack[-2] == pairs[c]:
            stack.pop()
            stack.pop()
    if len(stack) == 0:
        print("yes ")
    else:
        print("no ")


check("()()(")

check("()()()")

check("[(3 + 6)()]")

check("[(3 + } 6)()]")
