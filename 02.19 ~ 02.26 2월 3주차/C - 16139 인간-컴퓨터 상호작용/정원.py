import sys

input = sys.stdin.readline

S = input().strip()
prefix_sum = [[0]*26 for _ in range(len(S))]

for i in range(len(S)):
    for j in range(26):
        idx = ord(S[i])-97
        
        if idx == j:
            prefix_sum[i][j] = prefix_sum[i-1][j]+1
        else:
            prefix_sum[i][j] = prefix_sum[i-1][j]

for _ in range(int(input().strip())):
    A, L, R = input().strip().split()
    L, R = map(int, (L, R))

    idx = ord(A)-97
    result = prefix_sum[R][idx]
    if L != 0:
        result -= prefix_sum[L-1][idx]

    print(result)