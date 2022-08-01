def binary(start, end):
    global result, M
    if start > end: return
    budget = (start + end) // 2
    tmp = 0
    for b in B: tmp += min(b, budget)
    if tmp <= M:
        if budget > result: 
            result = budget
        binary(budget+1, end)
    else:
        binary(start, budget-1)

N = int(input())
B = sorted(list(map(int, input().split()))) # budget
M = int(input())
S, E = 0, M
result = 0
binary(S, E)
print(min(B[-1], result))