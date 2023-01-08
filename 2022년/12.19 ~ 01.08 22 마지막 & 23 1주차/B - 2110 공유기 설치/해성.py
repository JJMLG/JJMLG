import sys
sys.stdin = open("2110.txt")
def findValue(mid):
    cnt = 1
    start = arr[0]
    for num in arr:
        if num>= start+mid:
            cnt+=1
            start = num
    if cnt >= C:
        return 1
    else:
        return 0


N, C = map(int, input().split())
arr = sorted([int(input())for _ in range(N)])

start = 1
end = arr[-1]
maxval=-1
while start<=end:
    mid = (start + end)//2
    ret = findValue(mid)
    if ret:
        if maxval< mid:
            maxval = mid
        start = mid+1
    else:
        end=mid-1

print(maxval)