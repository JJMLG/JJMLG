for _ in range(int(input())):
    N = int(input())
    pa = [0] * (N + 1)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        pa[b] = a       # b의 부모는 a

    x, y = map(int, input().split())
    parent = set()      # a의 조상들
    while True:
        parent.add(x)
        if pa[x] == 0:  # 루트까지 오면 그만
            break
        x = pa[x]
    while True:
        if y in parent: # 공통 조상있으면 출력
            print(y)
            break
        y = pa[y]
