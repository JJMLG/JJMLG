from math import sqrt

def solution(k, d):
    ans = 0
    for x in range(0, d + 1, k):
        y = sqrt(d * d - x * x)
        ans += y // k + 1
    return ans
