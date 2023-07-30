def dfs(arr, visit, start):
    global cnt
    for nx in arr[start]:
        if not visit[nx]:
            visit[nx] = 1
            cnt += 1
            dfs(arr, visit, nx)

def solution(n, wires):
    global cnt
    answer = 987654321

    for i in range(len(wires)):
        wire = []
        for j in range(len(wires)):
            if i == j:
                continue
            wire.append(wires[j])
        arr = [[] for _ in range(n + 1)]
        
        for a, b in wire:
            arr[a].append(b)
            arr[b].append(a)
            
        visited = [0] * (n + 1)
        splited = []
        for nx in range(1, n + 1):
            if not visited[nx]:
                visited[nx] = True
                cnt = 1
                dfs(arr, visited, nx)
                splited.append(cnt)
        
        answer = min(answer, abs(splited[0] - splited[1]))
        
    return answer