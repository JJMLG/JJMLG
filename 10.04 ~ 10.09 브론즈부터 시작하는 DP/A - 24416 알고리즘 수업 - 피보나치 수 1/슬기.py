import sys
sys.stdin = open('input.txt')

n = int(input())


def fib(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fib(n - 1) + fib(n - 2)
    return 0

print(fib(n), n-2)