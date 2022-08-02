def binary(start, end):
    global result
    if start > end: return
    Blu_ray = (start + end) // 2
    tmp = [0] * M
    i = 0
    for l in L:
        if tmp[i] + l <= Blu_ray:
            tmp[i] += l
        else:
            i += 1
            try: tmp[i] += l
            except: binary(Blu_ray+1, end)
        if i>=M: break
    if i >= M: # 블루레이 개수가 모자람
        binary(Blu_ray+1, end)
    else: # i < M : 블루레이 크기를 더 줄일 수 있음
        if Blu_ray < result: result = Blu_ray
        binary(start, Blu_ray-1)

N, M = map(int, input().split())
L = list(map(int, input().split())) # lecture
S, E = max(L), sum(L)
result = int(1e9)
binary(S, E)
print(result)