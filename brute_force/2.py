"""
ГЕНЕРАЦИЯ ПЕРЕСТАНОВОК

Выведите все последовательности чисел от 1 до n, в которых каждое число встречается ровно 1 раз
"""

n = 7
a = list(range(1, n + 1))
used = [False for _ in range(n + 1)]


def rec(index):
    if index == n:
        print(*a, sep=' ')
        return
    for i in range(1, n + 1):
        if used[i]:
            continue
        a[index] = i
        used[i] = True
        rec(index + 1)
        used[i] = False


if __name__ == '__main__':
    rec(0)
