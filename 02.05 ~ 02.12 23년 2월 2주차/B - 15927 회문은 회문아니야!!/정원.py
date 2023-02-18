import sys

input = sys.stdin.readline

S = input().strip()
l = len(S)

if S == S[0]*l: print(-1)
elif S == S[::-1]: print(l-1)
else: print(l)

"""
Ad-Hoc(애드혹)
알고리즘 분류가 애드혹으로 되어있는 경우
주어진 문제를 구현하기보다, 창의적인 접근이 문제의 돌파구가 된다
"""