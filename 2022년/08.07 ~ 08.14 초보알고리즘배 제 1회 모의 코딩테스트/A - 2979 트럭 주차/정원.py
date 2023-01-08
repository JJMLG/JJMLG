P = [0] * 101 # parking
C = [0] + list(map(int, input().split())) # charge
for _ in range(3):
    I, O = map(int, input().split()) # in out
    for i in range(I, O): P[i] += 1
result = 0
for p in P:
    tmp = C[p] * p
    result += tmp
print(result)

"""
시간 : 13분
풀이
    트럭의 출입을 기록한 일지(P)를 만들고
    그 시간에 주차장에 있었던 트럭대수와
    요금을 곱해서 result++ 하여 출력
"""