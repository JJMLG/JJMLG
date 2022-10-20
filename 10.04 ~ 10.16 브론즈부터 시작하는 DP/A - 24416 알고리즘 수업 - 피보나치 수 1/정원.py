def fib(n):
    global result
    if n == 1 or n == 2:
        result += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)

N = int(input())
result = 0
fib(N)
print(result, N-2)