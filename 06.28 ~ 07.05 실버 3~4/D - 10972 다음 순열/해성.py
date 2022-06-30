import sys
sys.stdin = open('input.txt')
from itertools import permutations
N = int(input())
makeNumber = list(range(1,N+1))
prev = tuple(list(map(int, input().split())))

a = list(permutations(makeNumber, N))
if a.index(prev) == len(a)-1:
    print(-1)
else:
    print(*a[a.index(prev)+1])
