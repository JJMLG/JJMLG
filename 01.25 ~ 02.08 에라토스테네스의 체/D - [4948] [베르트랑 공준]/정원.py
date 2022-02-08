while True:
    N = int(input())
    if N == 0: # 종료 조건
        break
    
    n = 2 * N # 2n까지 소수를 구할 것

    # 에라토스테네스의 체
    a = [False,False] + [True]*(n-1)
    primes = []      
    for i in range(2,n+1):        
        if a[i]:                     
            primes.append(i)             
            for j in range(2*i, n+1, i): 
                a[j] = False             

    # 2n까지 구한 소수들을 순회하다가
    for i in range(len(primes)):
        if primes[i] > N: # n보다 커지는 구간이 나오면
            # 소수 전체 길이에서 구간시작 인덱스 빼기
            print(len(primes)-i)
            break
