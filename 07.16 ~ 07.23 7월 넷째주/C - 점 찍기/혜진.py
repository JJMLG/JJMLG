from math import sqrt

def solution(k, d):
    ans = 0
    for x in range(0, d + 1, k):    # x좌표
        y = sqrt(d * d - x * x)     # y좌표 최대 값
        ans += y // k + 1           # x좌표일 때 가능한 y좌표의 수를 더해줌
    return ans
