# 2346 풍선 터뜨리기
from collections import deque

N = int(input())
Q = deque(enumerate(map(int, input().split())))

ans = []
for _ in range(N):
    i, n = Q.popleft()
    ans.append(i + 1)
    if n > 0:   # 오른쪽으로 이동(오른쪽 pop, 0에 넣기)
        Q.rotate(-(n - 1))
    else:       # 왼쪽으로 이동(popleft, append)
        Q.rotate(-n)
print(*ans)
