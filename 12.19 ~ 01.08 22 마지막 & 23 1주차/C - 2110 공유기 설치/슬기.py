import sys
sys.stdin = open('input.txt')

n, c = map(int, input().split())
home = [int(input()) for _ in range(n)]
home.sort()

def binary_search(home):
    s = 1
    e = home[-1] - home[0]      # 집이 2개라면 무조건 처음, 마지막 집 사이의 거리

    while s <= e:
        mid = (s + e) // 2
        lan = 1
        # print(mid)
        now = home[0]   # 현재 설치된 공유기 위치(다음거랑 거리 비교해야 됨)
        for i in range(1, len(home)):
            if home[i] - now >= mid:
                now = home[i]
                lan += 1    # 공유기 개수 더해주기

        if lan >= c:
            s = mid + 1
        else:
            e = mid - 1
    return e

print(binary_search(home))