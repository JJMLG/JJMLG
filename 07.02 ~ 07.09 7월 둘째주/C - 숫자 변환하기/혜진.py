from heapq import heappush, heappop

def solution(x, y, n):
    arr = [-1] * (y + 1)
    arr[x] = 0
    hq = [(0, x)]
    while hq and arr[y] == -1:
        cnt, num = heappop(hq)
        for nn in [num + n, num * 2, num * 3]:
            if nn > y: continue
            if arr[nn] == -1:
                arr[nn] = cnt + 1
                heappush(hq, (cnt + 1, nn))
    return arr[y]
