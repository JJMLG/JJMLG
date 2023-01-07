def cut(length):
    cutted_cable = 0
    for cable in cables:
        cutted_cable += cable//length
    if cutted_cable >= N: return True
    else: return False

K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]
result = 1
start, end = result, sum(cables)//N
while start <= end:
    mid = (start + end)//2
    if cut(mid):
        result = max(result, mid)
        start = mid + 1
    else:
        end = mid - 1
print(result)