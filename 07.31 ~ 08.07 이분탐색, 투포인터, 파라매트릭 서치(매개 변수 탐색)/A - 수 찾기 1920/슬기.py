import sys
sys.stdin = open('input.txt')
sys.stdin.readline

n = int(input())
# a = set(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()

m = int(input())
arr_m = list(map(int, input().split()))

# for i in arr_m:
#     if i in a:
#         print(1)
#     else:
#         print(0)

def binary(find):
    # 시작 - 맨 왼쪽
    left = 0
    # 인덱스 맞추려고 맨 끝
    right = n-1

    while left <= right:
        # 중간 값
        mid = (left + right) // 2
        if a[mid] == find:
            return True

        if find < a[mid]:
            right = mid - 1
        elif find > a[mid]:
            left = mid + 1


for i in range(m):
    # 있으면
    if binary(arr_m[i]):
        print(1)
    # 없으면
    else:
        print(0)