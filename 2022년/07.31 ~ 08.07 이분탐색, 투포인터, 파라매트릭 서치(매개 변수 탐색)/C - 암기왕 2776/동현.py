t = int(input())
for _ in range(t):
    n = int(input())
    ls = sorted(list(map(int,input().split())))
    m = int(input())
    ls_2 = list(map(int,input().split()))


    for target in ls_2:
        flag = 0 
        start, end = 0, len(ls) - 1
        while start <= end:
            mid = ( start + end ) // 2
            if ls[mid] == target:
                flag = 1
                break

            if ls[mid] > target:
                end = mid -1
            else:
                start = mid +1
        
        
        if flag == 1:
            print(1)
        else:
            print(0)