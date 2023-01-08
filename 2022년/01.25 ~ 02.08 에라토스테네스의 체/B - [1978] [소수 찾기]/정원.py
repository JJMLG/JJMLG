# 문제에서 제공된 범위 N은 1000이하의 자연수
dp = [False, False] + [True] * (999) # 1000까지의 소수
primes = [] # 소수를 담을 리스트

for i in range(2, 1001): # 2부터 1000까지
    if dp[i]: # 소수다??
        primes.append(i) # 소수 리스트에 추가
        for j in range(i*2, 1001, i):
            # i의 배수는 전부 소수가 아니다
            dp[j] = False # 네

N = int(input())
nums = list(map(int, input().split()))

maxx = nums[-1] # 입력값들 중 가장 큰 값 : 맨 뒤 값
result = 0 # 출력할 소수의 개수

for p in primes: # 1000까지의 소수들 중
    for n in nums: # 입력받은 숫자들 중
        if n == p: # 같다면 : 소수라면
            if n == 1: # 근데 1은 소수가 아님
                continue # 패스
            result += 1 # 소수 개수 +1
    
    if p >= maxx: # 1000까지 구한 소수 전부 안돌고
        break # 마지막 입력값보다 현재 보는 소수가 크거나 같으면 
        # 종료

print(result) # 소수 개수 출력