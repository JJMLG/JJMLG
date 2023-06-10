ans = 0

def solution(k, dungeons):
    used = [0] * len(dungeons)

    def dfs(k, cnt):
        global ans
        ans = max(cnt, ans)
        for i in range(len(dungeons)):
            if used[i]: continue
            if dungeons[i][0] > k: continue
            used[i] = 1
            dfs(k - dungeons[i][1], cnt + 1)
            used[i] = 0
    
    dfs(k, 0)
    return ans
