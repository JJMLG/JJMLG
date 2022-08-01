def binary(t, s, e): # target, start, end
    if s > e: return 0
    i = (s+e) // 2 # index
    if t == arr1[i]: return 1
    elif t < arr1[i]: return binary(t, s, i-1)
    elif t > arr1[i]: return binary(t, i+1, e)

T = int(input())
for t in range(T):
    N = int(input())
    arr1 = list(map(int, input().split()))
    arr1.sort()
    M = int(input())
    arr2 = list(map(int, input().split()))
    for a in arr2:
        s, e = 0, N-1
        print(binary(a, s, e))