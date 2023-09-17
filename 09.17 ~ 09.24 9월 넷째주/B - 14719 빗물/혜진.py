H, W = map(int, input().split())
block = list(map(int, input().split()))
ans = 0

for i in range(1, W - 1):           # 양 사이드 제외
    lMax = max(block[:i])           # 왼쪽에서 제일 높은 벽
    rMax = max(block[i + 1:])       # 오른쪽에서 제일 높은 벽
    
    rain = min(lMax, rMax)          # 비로 채워지는 높이
    if rain > block[i]:             # 벽 높이보다 비 높이가 높으면
        ans += rain - block[i]      # 그만큼 빗물이 채워진다

print(ans)

###################################################################################################

H, W = map(int, input().split())
block = list(map(int, input().split()))
arr = [[0] * W for _ in range(H)]

for w in range(W):
    for h in range(block[w]):
        arr[H - 1 - h][w] = 1
# print(arr)

ans = 0
for c in range(W):
    for r in range(H - 1, -1, -1):
        if arr[r][c]: continue                          # 벽이면 pass
        if c == 0 or c == W - 1: continue               # 양 사이드는 pass
        if not (r == H - 1 or arr[r + 1][c]): continue  # 아래가 끝이거나 벽이여야 한다
        checkL = checkR = 0                             # 왼쪽과 오른쪽에 벽이 있어야 한다
        for x in range(W):
            if x == c: continue
            if x < c and arr[r][x]: checkL = 1
            if x > c and arr[r][x]: checkR = 1
            if checkL * checkR: break
        if checkL * checkR:
            arr[r][c] = 2
            ans += 1

print(ans)
