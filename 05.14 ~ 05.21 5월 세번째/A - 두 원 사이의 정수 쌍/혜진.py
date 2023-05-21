from math import floor, ceil

def solution(r1, r2):
    ans = 0
    
    for x in range(1, r2 + 1):
        maxR = floor((r2**2 - x**2)**0.5)
        minR = 0 if x >= r1 else ceil(abs(x**2 - r1**2)**0.5)
        ans += maxR - minR + 1
    
    return ans * 4
