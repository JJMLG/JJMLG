from heapq import heappush, heappop

def solution(n, paths, gates, summits):
    inf = 10000000 * n
    adj = [[] for _ in range(n + 1)]    # 인접리스트
    isSummit = [False] * (n + 1)        # 산봉우리인지 확인
    intensity = [inf] * (n + 1)         # i까지 갈 때 intensity값, 최소가 되어야 하니까 최대로 초기화하고 시작
    Q = []                              # 우선순위 큐 -> 기준은 intensity가 최소가 되도록

    for i, j, w in paths:
        adj[i].append((j, w))
        adj[j].append((i, w))

    for s in set(summits):
        isSummit[s] = True

    for g in gates:
        intensity[g] = 0                # (intensity값, 현재 위치)
        heappush(Q, (0, g))             # intensity가 최소가 되어야하니까 먼저 쓴다

    while Q:
        itst, v = heappop(Q)
        if isSummit[v]:                 # 산봉우리면 그만 -> 산봉우리까지 갈때의 intensity값을 구하기 위한 우선순위큐
            continue
        if itst > intensity[v]:         # 더 크면 그만 -> intensity값을 최소로 만들어야하니까
            continue
        
        for nv, nitst in adj[v]:
            nitst = max(intensity[v], nitst)    # 가장 큰 값 중에서
            if nitst < intensity[nv]:           # 최소로 만들어야 하니까 작은 경우만 확인, nv가 gate인 경우는 여기서 걸러짐
                intensity[nv] = nitst           # 작은 값으로 갱신
                heappush(Q, (nitst, nv))

    ans = [0, inf]
    for s in sorted(summits):           # intensity가 최소인 경우가 많으면 산봉우리번호가 작은걸 return해야하니까 정렬해서 확인
        if intensity[s] < ans[1]:       # 산봉우리까지 갈 때의 intensity값을 확인한다
            ans = [s, intensity[s]]
    return ans
