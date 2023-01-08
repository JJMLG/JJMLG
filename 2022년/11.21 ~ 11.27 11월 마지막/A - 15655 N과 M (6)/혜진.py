N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = [0] * M


def dfs(idx, cnt):
    if cnt == M:
        print(" ".join(map(str, ans)))
        return
    
    for j in range(idx, N):
        ans[cnt] = nums[j]
        dfs(j + 1, cnt + 1)


for i in range(N):
    ans[0] = nums[i]
    dfs(i + 1, 1)
