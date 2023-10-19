"""
ЧИСЛА ФИБОНАЧЧИ
"""


def fib(n):
    """
    ПЕРВЫЙ ВАРИАНТ
    """
    if n < 2:
        return n
    arr = [0 for _ in range(n + 1)]
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr[-1]


def fib2(n):
    """
    ВТОРОЙ ВАРИАНТ
    """
    if n < 2:
        return n
    prev1, prev2 = 0, 1
    for _ in range(2, n + 1):
        prev1, prev2 = prev2, (prev1 + prev2)
    return prev2


if __name__ == "__main__":
    print(fib2(10))
