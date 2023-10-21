"""
АЛГОРИТМ ЕВКЛИДА
Наибольший общий делитель
"""


def func(a: int, b: int):
    if a == 0 or b == 0:
        return max(a, b)
    if a >= b:
        return func(a % b, b)
    else:
        return func(b % a, a)


if __name__ == '__main__':
    print(func(100, 45))

