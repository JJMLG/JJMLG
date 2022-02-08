N, K = map(int, input().split())

# N까지 소수인지 아닌지 확인할 DP배열
dp = [False, False] + [True] * (N-1)
cnt = 0 # 몇번째 지워지는 수인지 세기 위한 cnt

for i in range(2, N+1): # 2부터 시작
    if dp[i]: # 소수라면?
        for j in range(i, N+1, i): # i의 배수는 전부 소수아님
            # 그래서 i의 배수를 전부 지울건데
            # 지운걸 또 지울 수 없음
            # ex) 6은 2의 배수에서 지워지는데 3의배수에도 걸림
            if dp[j]: # 그래서 안지워졌는지 확인하고
                dp[j] = False # 지우면서
                cnt += 1 # cnt 1 더하기
                if cnt == K: # K번째로 지울 때
                    print(j) # 그 값을 출력
                    exit() # 코드 종료
