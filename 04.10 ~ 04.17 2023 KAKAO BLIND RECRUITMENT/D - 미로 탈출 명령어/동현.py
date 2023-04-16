def solution(n, m, x, y, r, c, k):
    
    dir = ['i','r','u','d']
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    result = []
    def dfs(i,j,cnt,ls):
        print(ls)
        if cnt > k:
            return
        if abs(i-r) + abs(j-c) > k-cnt:
            return
        
        if cnt == k:
            if i == r and j == c:
                result.append(ls[:])
            return
        for t in range(4):
            nx = i + dx[t]
            ny = j + dy[t]
            if 0 <= nx < n and 0 <= ny < m:
                dfs(nx,ny,cnt+1,ls + dir[t])
    
    dfs(x,y,0,"")
    answer = ''
    print(result)
    return answer