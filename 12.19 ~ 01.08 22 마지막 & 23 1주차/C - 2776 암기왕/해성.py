def binarySearch(num):
    start = 0
    end = N-1
    while start <= end:
        mid = (start+end)//2
        if num == book1[mid]:
            return 1
        if num < book1[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    book1 = sorted(list(map(int, input().split())))

    M = int(input())
    book2 = list(map(int, input().split()))

    for num in book2:
        if(binarySearch(num)):
            print(1)
        else:
            print(0)