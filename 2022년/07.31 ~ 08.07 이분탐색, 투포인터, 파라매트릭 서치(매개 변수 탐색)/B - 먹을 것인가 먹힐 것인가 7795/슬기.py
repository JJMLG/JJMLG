import sys
sys.stdin = open('input.txt')


def binary(ls_b, compare):
    start, end = 0, len(ls_b)-1
    res = -1

    while start <= end:
        mid = (start + end) // 2
        if ls_b[mid] < compare:
            res = mid
            start = mid + 1
        else:
            end = mid - 1
    return res


t = int(input())

for _ in range(t):
    a_n, b_m = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_a.sort()
    arr_b = list(map(int, input().split()))
    arr_b.sort()
    visited = [0] * len(arr_a)

    cnt = 0
    for i in arr_a:
        cnt += (binary(arr_b, i) + 1)
    print(cnt)