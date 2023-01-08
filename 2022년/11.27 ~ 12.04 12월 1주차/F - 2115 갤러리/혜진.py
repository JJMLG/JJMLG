N, M = map(int, input().split())        # 세로, 가로
arr = [list(input()) for _ in range(N)]
pic = [[set() for _ in range(M)] for _ in range(N)]
cnt = 0

for n in range(1, N):
    for c in range(1, M):
        if arr[n][c] == ".":

            if arr[n][c + 1] == ".":    # 가로
                if arr[n - 1][c] == "X" and arr[n - 1][c + 1] == "X" and "U" not in pic[n][c] and "U" not in pic[n][c + 1]:
                    cnt += 1
                    pic[n][c].add("U")
                    pic[n][c + 1].add("U")
                if arr[n + 1][c] == "X" and arr[n + 1][c + 1] == "X" and "D" not in pic[n][c] and "D" not in pic[n][c + 1]:
                    cnt += 1
                    pic[n][c].add("D")
                    pic[n][c + 1].add("D")

            if arr[n + 1][c] == ".":  # 세로
                if arr[n][c - 1] == "X" and arr[n + 1][c - 1] == "X" and "L" not in pic[n][c] and "L" not in pic[n + 1][c]:
                    cnt += 1
                    pic[n][c].add("L")
                    pic[n + 1][c].add("L")
                if arr[n][c + 1] == "X" and arr[n + 1][c + 1] == "X" and "R" not in pic[n][c] and "R" not in pic[n][c + 1]:
                    cnt += 1
                    pic[n][c].add("R")
                    pic[n + 1][c].add("R")

print(cnt)
