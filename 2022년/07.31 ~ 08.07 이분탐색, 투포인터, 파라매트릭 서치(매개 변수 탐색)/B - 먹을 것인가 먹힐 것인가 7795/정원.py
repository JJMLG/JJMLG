T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())), reverse=True)
    B = sorted(list(map(int, input().split())), reverse=True)
    i = j = 0
    result = 0
    while i<N and j<M:
        if A[i] > B[j]:
            result += M-j
            i += 1
        else:
            j += 1
    print(result)