def install_wifi(distance):
    prev = houses[0]
    cnt = 1
    for house in houses[1:]:
        if house>=prev+distance:
            cnt += 1
            prev = house
    return cnt

N, C = map(int, input().rstrip().split())
houses = sorted([int(input().rstrip()) for _ in range(N)])
result = 0
start, end = result, houses[-1]
while start<=end:
    mid = (start + end)//2
    if install_wifi(mid)>=C:
        result = max(result, mid)
        start = mid+1
    else: 
        end = mid-1
print(result)

"""
다음 집을 탐색할 때, 다음 집이 위치한 인덱스만 확인함
"""