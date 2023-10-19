"""
ПРАВИЛЬНЫЕ СКОБОЧНЫЕ ПОСЛЕДОВАТЕЛЬНОСТИ

Проверить скобочную последователь на правильность
"""

s1 = '((())())))'
s2 = '(())(())()'
s3 = '(()))((())'
s4 = '((((())))'
s5 = '(()())(())'


def rec(s):
    balance = 0
    for i in s:
        if i == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False
    return balance == 0


if __name__ == '__main__':
    print(rec(s1), rec(s2), rec(s3), rec(s4), rec(s5))
