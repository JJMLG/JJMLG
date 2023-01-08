import sys

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
P = ['' for _ in range(N+1)] # pokemon
for n in range(1, N+1): P[n] = input()
for m in range(M):
    Q = input()
    try: print(P[int(Q)])
    except: print(P.index(Q))

"""
1. 빠른 입력 없을 시 시간초과
2. 포켓몬 리스트를 선입력하지 않고, append를 통해 만들 시 시간초과
"""