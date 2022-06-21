"""
실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수 
N = 전체 스테이지
stages = 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열
실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return
1 <= N <= 500
1 <= len(stages) <= 200,000
1 <= stages[i] <= N+1
stages[i] = 도전중인 스테이지 번호
if stages[i] == N+1:
    마지막 스테이지까지 클리어
500스테이지까지 있으며, 배열의 값이 501일 경우 500층을 클리어, 게임 클리어
실패율이 같을 경우 스테이지 번호 오름차순
if 해당 스테이지에 도달한 유저가 없음:
    실패율 = 0
ex)
    N = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3] # 6은 5단계를 전부 클리어한 사람
    result = [3, 4, 2, 1, 5]
    필요한 것
        1. i번 스테이지 클리어하지 못한 사람 배열 # Fail
            # F = [1, 3, 2, 1, 0] 
        2. i번 스테이지를 도전한 사람 배열 # Challenge
            # C = [8, 7, 4, 2, 1] 
        3. 스테이지별 실패율 튜플 배열 # fail Rate
            # R = [(1, 0.125), (2, 0.428), (3, 0.5), (4, 0.5), (5, 0)] 
    실패율 배열 lambda로 내림차순 정렬
    정렬된 배열을 answer에 담아서 반환
"""

def solution(N, stages):
    answer = []
    F = [0] * N # 클리어하지 못한 사람
    C = [0] * N # 도전한 사람
    R = [] # 실패율
    for i in range(len(stages)):
        if stages[i] <= N:
            F[stages[i]-1] += 1
        for j in range(stages[i], 0, -1):
            if j <= N:
                C[j-1] += 1
    for n in range(N):
        rate = 0
        if C[n] != 0: # Zero Division 에러 회피
            rate = F[n]/C[n]
        R.append((n+1, rate))     
    R.sort(key=lambda x:x[1], reverse=True)
    answer = list(r for r, n in R)
    return answer
