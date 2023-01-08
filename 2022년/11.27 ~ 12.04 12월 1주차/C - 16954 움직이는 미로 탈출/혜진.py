arr = [input() for _ in range(8)]
d = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (0, 0)]

def bfs():
    new = []
    for r, c in Q:
        if r == 0:              # 0행이면 제일 오른쪽에 갈 수 있다
            return 1

        if arr[r][c] == ".":    # 움직인 뒤 벽이 내려왔으면 pass 아니면 ㄱㄱ
            for dr, dc in d:
                nr, nc = r + dr, c + dc
                if 0 <= nr < 8 and 0 <= nc < 8 and arr[nr][nc] == ".":
                    new.append((nr, nc))
    return new

Q = [(7, 0)]
ans = 0
while Q and not ans:
    Q = bfs()

    if Q == 1:
        ans = 1

    arr = ["........"] + arr[:7]

print(ans)                      # 모든 경우에 벽이라서(10번줄) Q가 끝나버리면 0이 출력
