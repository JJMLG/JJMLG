"""
**이분탐색으로 찾는것: 집들 사이의 최소거리(m)
    => s는 최소 거리인 1, e는 최대 거리인 H[-1] - H[0]

최소거리를 m으로 두고 H를 돌면서 확인한다
    => 집 사이 거리가 m보다 짧으면 pass
    => 아니면 cnt + 1하고 기준 집 변경

다 돌았을 때 cnt가 C보다 작으면 최소 거리가 줄어야 하니 e를 왼쪽으로: m - 1
아니면 s를 m + 1로 하고 일단 결과값 ans에 m 저장해두기
"""

def binarysearch(s: int, e: int):
    ans = 0

    while s <= e:
        m = (s + e) // 2
        now = H[0]          # 마지막에 공유기 설치한 집
        cnt = 1             # 공유기 설치한 집의 수

        for i in range(1, N):
            if H[i] - now < m: continue
            cnt += 1
            now = H[i]

        if cnt >= C:
            ans = m
            s = m + 1
        else:
            e = m - 1

    return ans

N, C = map(int, input().split())
H = [int(input()) for _ in range(N)]
H.sort()

print(binarysearch(1, H[-1] - H[0]))
