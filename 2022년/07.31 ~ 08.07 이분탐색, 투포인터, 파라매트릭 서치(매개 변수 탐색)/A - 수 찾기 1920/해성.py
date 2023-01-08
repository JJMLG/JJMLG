import sys
sys.stdin = open('input.txt')

N = int(input())
NS = sorted(list(map(int, input().split())))
M = int(input())
MS = list(map(int, input().split()))

for num in MS:
    s, e = 0, N-1
    l = s
    r = N - 1
    while l<=r:
        mid = (l+r)//2
        if (NS[mid] == num):
            print(1)
            break
        else:
            if (NS[mid]>num):
                r= mid-1
            else:
                l=mid+1
    if NS[mid]!=num:
        print(0)


# for num in MS:
#     lt, rt = 0, N-1
#     isExist = 0
#     while lt<= rt:
#         mid = (lt+rt)//2
#         if num == NS[mid]:
#             isExist=1
#             print(1)
#             break
#         elif num> NS[mid]:
#             lt = mid+1
#         else:
#             rt = mid-1
#
#     if not isExist:
#         print(0)