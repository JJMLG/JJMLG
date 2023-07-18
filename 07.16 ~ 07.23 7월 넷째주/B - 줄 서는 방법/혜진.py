from math import factorial

def solution(n, k):
    ans = []
    arr = [i for i in range(1, n + 1)]
    k = k - 1
    
    while arr:
        x = k // factorial(n - 1)
        ans.append(arr[x])
        del arr[x]
        
        k %= factorial(n - 1)
        n -= 1
    return ans
