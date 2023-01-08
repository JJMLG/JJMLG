import sys

input = sys.stdin.readline

N = int(input())
result = 0
for n in range(N):
    W, S = input().rstrip(), [] # word, stack
    for w in W:
        if S and w == S[-1]: S.pop() # 스택 마지막과 같으면 pop
        else: S.append(w) # 다르면 append
    if not S: result += 1 # 다 짝이 맞아서 스택에 남은게 없으면 result++
print(result)