def calc(op, sub, num) -> int:
    if op == '+':
        return sub + num
    elif op == '-':
        return sub - num
    elif op == '*':
        return sub * num
    # 나누기가 좀 특이한데, 문제에 나와있는 그대로 구현
    if sub < 0:
        return -((-sub) // num)
    return sub // num

def recur(nIdx, sub):               # 현재 사용한 숫자의 수, 계산결과값
    if nIdx == N:                   # N개의 숫자를 모두 계산하면 정답 갱신하고 return
        global M, m
        if M < sub: M = sub
        if m > sub: m = sub
        return
    for i in range(N - 1):
        if u[i]: continue           # 사용하지 않은 연산자만 -> 순열
        u[i] = 1
        recur(nIdx + 1, calc(operator[i], sub, A[nIdx]))
        u[i] = 0

N = int(input())
A = list(map(int, input().split()))
operator = []
for i, v in enumerate(map(int, input().split())):
    for _ in range(v):
        operator.append('+-*/'[i])  # 해당 연산자를 개수만큼 배열에 추가

M = -1000000000
m = 1000000000
u = [0] * N
recur(1, A[0])
print(M)
print(m)
