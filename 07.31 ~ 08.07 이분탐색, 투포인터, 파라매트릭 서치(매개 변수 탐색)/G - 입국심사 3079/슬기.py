import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
time = [int(input()) for _ in range(n)]

start = 0
end = min(time) * m     # time의 최솟값 * 사람수 = 최대시간

result = 0

while start <= end:
    mid = (start + end) // 2
    temp = 0

    for i in time:
        temp += mid // i

    if temp >= m:
        end = mid - 1
        result = mid
    else:
        start = mid + 1

print(result)