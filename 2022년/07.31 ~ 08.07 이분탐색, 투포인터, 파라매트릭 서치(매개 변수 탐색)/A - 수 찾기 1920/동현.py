import sys

sys.stdin=open('input.txt')

n = int(input())
ls = sorted(list(map(int,input().split())))
m = int(input())
ls_2 = list(map(int,input().split()))


def search(start,end,target):
    
    while start <= end:
        mid = (start + end ) // 2

        if ls[mid] == target:
            return 1
        
        if ls[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return 0
#  1 2 3 4 5

for i in ls_2:
    print(search(0,n-1,i))
