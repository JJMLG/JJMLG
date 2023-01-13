from collections import deque

N, K = map(int, input().split())

# 왼쪽으로 가는건 한칸씩 이동밖에 없음
if K <= N:
    print(N - K)
    exit()

# 2*X로 이동할 수 있으니까 범위는 20000+1까지, value = idx까지 가는데 걸리는 시간
sec = [987654321] * 200001
Q = deque([(0, N)])
sec[N] = 0

while Q:
    t, v = Q.popleft()
    for nt, nv in ((t + 1, v - 1), (t + 1, v + 1), (t, v * 2)):
        # nv가 범위 안이고, 더 빨리 갈 수 있으면
        if 0 <= nv < 200001 and nt < sec[nv]:
            sec[nv] = nt
            Q.append((nt, nv))

print(sec[K])
