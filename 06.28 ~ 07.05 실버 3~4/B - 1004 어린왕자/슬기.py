import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    planet = int(input())

    cnt = 0
    for _ in range(planet):
        cx, cy, r = map(int, input().split())

        # 점과 점 사이의 거리 구하는 공식 루트(x2-x1)제곱 + (y2-y1)제곱
        start = (((x1 - cx) ** 2) + ((y1 - cy) ** 2)) ** 0.5
        end = (((cx - x2) ** 2) + ((cy - y2) ** 2)) ** 0.5

        # 시작 도착이 행성 내부인 경우 > 다른 행성 진입 필요 없음
        if start < r and end < r:
            pass

        # 하나만 행성 내부에 있는 경우 진입이나 탈출 필요
        elif start < r:
            cnt += 1
        elif end < r:
            cnt += 1
    print(cnt)



"""
문제 이해를 못 하겠음!


그 다음 줄부터 각각의 테스트케이스에 대해 첫째 줄에 출발점 (x1, y1)과 도착점 (x2, y2)이 주어진다. 
두 번째 줄에는 행성계의 개수 n이 주어지며, 세 번째 줄부터 n줄에 걸쳐 행성계의 중점과 반지름 (cx, cy, r)이 주어진다.
"""