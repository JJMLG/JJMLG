import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())        # N가지 캔, K일동안 준다
A = list(map(int, input().split()))     # i번째 캔 A[i]개 있다
R = [list(map(int, input().split())) for _ in range(K)] # 랑이 만족도
M = [list(map(int, input().split())) for _ in range(K)] # 메리 만족도

ans = 0
def DFS(cur, sat):              # 며칠째, 만족도 합
    if cur == K:                # K일 끝났으면
        global ans
        ans = max(ans, sat)     # 갱신
        return
    
    for r in range(N):
        if A[r] == 0: continue  # 캔이 없으면 넘어간다
        A[r] -= 1               # 있으면 준다
        for m in range(N):
            if A[m] == 0: continue
            A[m] -= 1
            DFS(cur + 1, sat + R[cur][r] + M[cur][m])
            A[m] += 1           # 되돌린다
        A[r] += 1

DFS(0, 0)
print(ans)
