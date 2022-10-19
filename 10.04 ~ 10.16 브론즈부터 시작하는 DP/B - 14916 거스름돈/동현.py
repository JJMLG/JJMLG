import sys

n = int(input())
f = [0]*(n+1)
f[1] = 1
f[2] = 1
def fib(n):

    if n == 1 or n ==2:
        return 1
    
    else:
        return fib(n-1) + fib(n-2)

def fib_2(n):

    for i in range(3,n+1):
        f[i] = f[i-1] + f[i-2]
    
    return f[n]

print(fib(n),n-2)
