t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = sorted(list(map(int,input().split())))
    b = sorted(list(map(int,input().split())))
    cnt  = 0 


    for target in a:
        start, end = 0 , len(b)-1
        res = -1
        
        while start <= end:

            mid = (start + end ) // 2
            
            # if b[mid] == target:
            #     pass

            if b[mid] >= target:
                end = mid - 1
            
            else:
                res = mid
                start = mid + 1
        # print(res,'흠')
        cnt += (res + 1)

    print(cnt)