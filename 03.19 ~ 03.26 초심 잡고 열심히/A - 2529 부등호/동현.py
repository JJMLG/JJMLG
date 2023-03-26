
from collections import deque
import sys
from itertools import combinations
from pprint import pprint
sys.stdin = open('input.txt')


n,b,a =  map(int,input().split())
ls =  list(map(int,input().split()))
ls.sort()

ans = 0
for price in ls:
    if b-price >= 0:
        b -= price
        ans += 1
    else:
        if a > 0 and b-price/2 >= 0:
            a -= 1
            b -= price/2
            ans += 1
print(ans)
