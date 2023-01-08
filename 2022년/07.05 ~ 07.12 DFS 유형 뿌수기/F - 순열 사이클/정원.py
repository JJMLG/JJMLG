for _ in range(int(input())):
    N = int(input())
    P = [list(range(1, N+1)), list(map(int, input().split()))]
    used, result = [0] * N, 0
    for i in range(N):
        if not used[i]:
            used[i], start, now = 1, P[0][i], P[1][i]
            while now != start:
                used[now-1] = 1
                now = P[1][now-1]
            result += 1
    print(result)

"""
문제 조건이, 1부터 N까지의 자연수로 이루어졌다고 
주어졌기 때문에, 한 사이클을 돌 때 인덱스를 고민하지 않아도 되었다
"""