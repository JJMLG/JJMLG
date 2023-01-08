def binary(start, end):
    global result, M
    if start > end: return # 탐색 범위를 벗어남
    budget = (start + end) // 2 # 이번에 탐색해볼 예산
    tmp = 0 # 해당 예산으로 도시들마다 예산 지급시 총 금액
    for b in B: tmp += min(b, budget)
    if tmp <= M: # 예산을 다 지급했는데 아직 여유가 있다면
        if budget > result: # 그 예산이 기존 최대 예산보다 크다면
            result = budget # 최대값 갱신
        binary(budget+1, end) # 다음 큰 범위 탐색
    else: # 해당 예산으로 지급 시, 총 예산을 초과한다면
        binary(start, budget-1) # 다음 작은 범위 탐색

N = int(input())
B = sorted(list(map(int, input().split()))) # budget
M = int(input()) # 총 예산
S, E = 0, M # 이분탐색은 매우 효율적인 알고리즘이므로 범위 시작과 끝을 무지성으로 지정해도 잘 돌아간다
result = 0 # 결과값 초기화
binary(S, E) # 이론상 최대 예산을 구하기
# 모든 도시의 예산의 합이 전체 예산보다 클 경우 가장 큰 예산을 출력
print(min(B[-1], result)) 