for _ in range(int(input())):
    N = int(input())
    X = list(map(int, input().split()))
    dic = { x: 1 for x in X }               # 이렇게 하면 정렬할 필요가 없다
    ans = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            bb = X[i] + X[j]                # 아무거나 두개 뽑아서 a, b, c 중 아무거나로 생각해도 된다
            if bb % 2: continue             # dic 확인 덜하려고 a, c를 뽑았다고 가정함
            if dic.get(bb//2, 0):
                ans += 1
    print(ans)

############################################################################################################

# 이분탐색
def binarySearch(lst, target, si, ei) -> bool:  # -> bool 이거 했다고 속도에 차이가 있다..아주 조금
    while si <= ei:
        midIdx = (si + ei) // 2
        if lst[midIdx] == target:
            return True
        if lst[midIdx] > target:
            ei = midIdx - 1
        else:
            si = midIdx + 1
    return False

for _ in range(int(input())):
    N = int(input())
    X = list(map(int, input().split()))
    X.sort()
    ans = 0
    for i in range(N - 2):                  # a가 가능한 범위: 0 ~ N-3
        a = X[i]
        for j in range(i + 2, N):           # c가 가능한 범위: a두칸뒤 ~ N-1
            c = X[j]
            if abs(a + c) % 2: continue     # 중간값이 자연수가 아니면 pass
            if binarySearch(X, (a + c) // 2, i, j):
                ans += 1
    print(ans)

############################################################################################################

# 시간초과(1%)
for _ in range(int(input())):
    N = int(input())
    X = list(map(int, input().split()))
    X.sort()
    ans = 0
    for i in range(N - 2):
        a = X[i]
        for j in range(i + 1, N - 1):
            b = X[j]
            for k in range(j + 1, N):
                c = X[k]
                if b - a > c - b:           # 앞의 차이가 더 크면 c를 증가시켜야 한다
                    continue
                if b - a == c - b:          # 같으면 추가
                    ans += 1
                break                       # 같거나 크면 더이상 볼 필요 없다
    print(ans)
