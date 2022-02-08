N = int(input())

if N == 1:
    # 놀랍게도 1은 소수가 아니었다!!
    cnt = 0
else:
    # 에라토스테네스의 체로 N까지의 소수 구하기
    a = [False,False] + [True]*(N-1)
    primes = []
    for i in range(2,N+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, N+1, i):
                if a[j]:
                    a[j] = False

    # 투포인터에 사용할 변수 s, e와
    # 연속합이 N일때 카운트할 cnt
    s = e = cnt = 0

    # 가장 작은 소수부터 시작
    now = 2

    while True:
        # 투포인터 탐색 종료조건
        if (now < N and e == len(primes)-1) or (now > N and s == len(primes)-1):
            break

        if now == N: # 구간합이 N과 같으면
            cnt += 1 # 카운트 증가
            now -= primes[s] # 포인터 이동
            s += 1
        elif now < N: # 구간합이 N보다 작을 때
            e += 1 # 한 칸 밀어주기
            now += primes[e]
        elif now > N: # 구간합이 N보다 클 때
            now -= primes[s]
            s += 1 # 한 칸 땡겨주기

    if now == N: # 다 돌고 마지막 본인이 소수일 때
        cnt += 1 # 카운트 증가

print(cnt)