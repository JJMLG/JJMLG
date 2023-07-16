def solution(n):
    arr = [[0] * i for i in range(1, n + 1)]
    
    r, c = -1, 0
    curr = 1
    for d in range(n):
        for _ in range(d, n):
            if d % 3 == 0:      # 아래로
                r += 1
            elif d % 3 == 1:    # 오른쪽으로
                c += 1
            else:               # 위로
                r -= 1
                c -= 1
            arr[r][c] = curr
            curr += 1

    ans = []
    for ar in arr:
        ans += ar
    return ans

print(solution(4))