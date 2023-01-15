def binary(n):
    s, e = 0, N - 1
    while s <= e:
        m = (s + e) // 2
        if gap[m] < n:
            e = m - 1
        else:
            s = m + 1
    return e

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
_ = int(input())
W = map(int, input().split())

gap = [0] * N
gap[0] = A[0] - B[0]
for i in range(1, N):
    gap[i] = gap[i - 1] if gap[i - 1] < A[i] - B[i] else A[i] - B[i]

for w in W:
    print(binary(w) + 1)
