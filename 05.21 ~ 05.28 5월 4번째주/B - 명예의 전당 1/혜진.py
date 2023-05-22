from heapq import heappush, heappop

def solution(k, score):
    ans = []
    Q = []                          # 명예의 전당
    for s in score:
        if len(Q) < k:              # 무조건 추가
            heappush(Q, s)
        elif s > Q[0]:              # 점수가 가장 낮은사람 빼고 추가
            heappop(Q)
            heappush(Q, s)
        ans.append(Q[0])            # 발표는 점수 가장 낮은 사람
        
    return ans
