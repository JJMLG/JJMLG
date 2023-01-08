import sys
sys.stdin = open('input.txt')

def bisearch(A,b):
    start, end = 0, len(A)-1
    while start<=end:
        mid = (start + end) // 2
        if (A[mid]==b):
            return 1
        elif A[mid] < b:
            start = mid+1
        else:
            end = mid-1


    if A[mid]!= b:
        return 0

T = int(input())

for TC in range(1,T+1):
    N = int(input())
    A = sorted(list(map(int, input().split())))
    M = int(input())
    B = list(map(int, input().split()))
    for b in B:
        print(bisearch(A, b))
