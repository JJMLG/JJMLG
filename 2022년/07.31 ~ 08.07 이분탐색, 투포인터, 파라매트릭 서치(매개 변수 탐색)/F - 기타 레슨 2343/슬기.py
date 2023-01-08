import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
lecture = list(map(int, input().split()))

start = max(lecture)    # 하나의 비디오에 다 담을 수 있을 때
end = sum(lecture)      # 비디오가 가질 수 있는 가장 작은 크기

result = 10 ** 9
while start <= end:
    mid = (start + end) // 2
    size = 0
    cnt = 1

    for i in lecture:
        if size + i <= mid:
            size += i
        else:
            cnt += 1
            size = i
            if cnt > m:
                break

    # 비디오 수가 많으면 사이즈를 늘림
    if cnt > m:
        start = mid + 1
    # 비디오 수가 적으면 비디오 크기를 늘림
    else:
        end = mid - 1
        if mid >= start:
            result = min(result, mid)

print(result)