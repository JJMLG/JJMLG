from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline


arr = [input() for _ in range(5)]
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
ans = 0


def isConnect(lst):                             # 7명의 index가 담긴 배열
    visitied = [[1] * 5 for _ in range(5)]      # 일단 모두 1로
    for r, c in lst:
        visitied[r][c] = 0                      # 7명은 0으로

    sr, sc = lst[0]
    Q = deque([(sr, sc)])                       # 아무나 한명을 기준으로 연결되어 있는지 확인
    visitied[sr][sc] = 1                        # 방문 체크 표시
    tot = 1                                     # 총 몇명 연결되어 있는가?
    S = 1 if arr[sr][sc] == 'S' else 0          # S는 몇 명인가?

    while Q:
        r, c = Q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 5 and 0 <= nc < 5 and not visitied[nr][nc]:
                visitied[nr][nc] = 1
                Q.append((nr, nc))
                tot += 1
                if arr[nr][nc] == 'S': S += 1

        if tot - S > 3: return 0                # Y가 3보다 크면 칠공주 결성 실패

    if tot == 7 and S > 3: return 1             # 7명이 모두 연결되어있고, S가 4명 이상이면 성공
    return 0                                    # 아니면 실패


def makeIndex(num):
    r, c = divmod(num, 5)
    return r, c


for cb in combinations(range(25), 7):           # 25명 중에 7명을 중복없는 조합으로 뽑기
    lst = [makeIndex(n) for n in cb]            # 숫자를 index로 바꿔서 배열에 담기
    ans += isConnect(lst)                       # 연결되어 있고, S가 더 많으면 +1

print(ans)
