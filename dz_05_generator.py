# Написать генератор, который при каджом обращении к нему генерирует элемент последовательности 1, 2, 3, 4, 5, 6... , 
# но ! если генерируемый элемент делится на 3 без остатка - возвращает вместо него "Василий"

from tkinter import Y


def genetator(x):
     for i in range(1,20):
        if i%3 == 0:
            yield 'Василий'
        elif i%2 == 0:
            yield 'Георгий'
        else:
            yield i

m = genetator(0)
for i in range(19):
    print(next(m))
