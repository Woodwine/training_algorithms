"""
АЛГОРИТМ ЕВКЛИДА
Наибольший общий делитель
"""


def func(a: int, b: int):
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return func(a % b, b)
    else:
        return func(a, b % a)


if __name__ == '__main__':
    print(func(100, 45))
