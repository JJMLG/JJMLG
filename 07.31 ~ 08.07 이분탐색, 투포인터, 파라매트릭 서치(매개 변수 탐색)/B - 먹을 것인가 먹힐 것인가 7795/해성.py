import sys
sys.stdin = open('input.txt')
T = int(input())
def bisearch(B,a):
    global pos
    pos=0
    start, end = 0, len(B)-1
    while start<=end:
        mid = (start + end) // 2
        if B[mid] < a:
            pos = mid
            start = mid+1
        else:
            end = mid-1
    return pos +1

for TC in range(1,T+1):
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = sorted(list(map(int, input().split())))
    cnt=0
    for a in A:
        if a<=B[0]:
            continue
        else:
            cnt += bisearch(B, a)
    print(cnt)


