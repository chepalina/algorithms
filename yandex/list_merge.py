"""
Даны $k$ отсортированных в порядке неубывания массивов неотрицательных целых чисел,
каждое из которых не превосходит 100. Требуется построить результат их слияния:
отсортированный в порядке неубывания массив,
содержащий все элементы исходных $k$ массивов. Длина каждого массива не превосходит $10\cdot k$.
"""


m1 = [1, 2, 3]
m2 = [1, 1, 1]
m3 = [100]

m_list = [m1, m2, m3]

# pointers = [0] * len(m_list)

counter = {i: 0 for i in range(101)}

for l in m_list:
    for element in l:
        counter[element] += 1


target = []
for key, value in counter.items():
    if value > 0:
        target.extend([key] * value)


print(target)


dict = {1: 0, 0: 1, 3: 10}

print({key: 0 for key in range(-100, 101)})
d = {key: 0 for key in range(-100, 101)}


print(d.get(5))
