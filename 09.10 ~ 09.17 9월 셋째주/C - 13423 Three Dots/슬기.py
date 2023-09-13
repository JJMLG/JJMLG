t = int(input())
for _ in range(t):
    n = int(input())
    pos = list(map(int, input().split()))
    pos.sort()
    cnt = 0

    dic_pos = {}
    for i in pos: dic_pos[i] = 1

    for i in range(n-1):
        for j in range(i+1, n):
            # third = 2*pos[j] - pos[i]
            gap = pos[j] - pos[i]
            try:
                if dic_pos[pos[j] + gap]:
                    cnt += 1
            except:
                continue
    print(cnt)