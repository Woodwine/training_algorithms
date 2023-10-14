"""
РАЗБИЕНИЕ ЧИСЕЛ НА СЛАГАЕМЫЕ
"""

n = 35

a = [0 for _ in range(n)]


def rec(index, summ, last):
    if summ == n:
        print(*a[:index], sep=' ')
        return
    for i in range(last, n - summ + 1):
        a[index] = i
        rec(index + 1, summ + i, i)


if __name__ == '__main__':
    rec(0, 0, 1)
