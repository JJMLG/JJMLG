K, N = map(int, input().split())
L = [int(input()) for _ in range(K)]

s, e = 1, max(L)

while s <= e:
    m = (s + e) // 2
    cnt = 0                 # 총 랜선 수

    for l in L:
        cnt += l // m       # 자른 랜선 수

    if cnt >= N:            # 총 랜선 수가 더 많으면 s 를 오른쪽으로
        s = m + 1
    else:                   # 적으면 e를 왼쪽으로
        e = m - 1

print(e)
