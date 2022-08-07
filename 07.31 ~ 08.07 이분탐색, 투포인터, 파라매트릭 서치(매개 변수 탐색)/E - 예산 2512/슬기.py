import sys
sys.stdin = open('input.txt')

city = int(input())
request = list(map(int, input().split()))
budget = int(input())

start = 0
end = max(request)


while start <= end:
    mid = (start + end) // 2
    limit = 0       # 총 지출 양
    # print(mid)
    for i in request:
        if i > mid:
            limit += mid
            # print(limit, '///22')
        else:
            limit += i
            # print(limit,'---333')
    # 예산 남으면 상한선을 늘리고
    if limit <= budget:
        start = mid + 1
    # 예산 초과면 상한선을 줄임
    else:
        end = mid - 1
print(end)


"""
특정한 정수 상한액을 구해야 됨
상한액을 초과한 경우 > 상한액으로 바꿔주기
예산 보다 작아도 됨
"""