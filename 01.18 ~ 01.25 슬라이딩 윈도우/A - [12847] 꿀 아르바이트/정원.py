N, M = map(int, input().split())

# 급여 정보 입력
pays = list(map(int, input().split()))

s = 0 # 창문의 시작과
e = M-1 # 끝

# 결과값과 윈도우값 초기화
result = window = sum(pays[s:e+1])

while e < N-1: # 윈도우 이동을 종료하는 조건
    # 윈도우 한 칸 이동~~
    window -= pays[s]
    s += 1
    e += 1
    window += pays[e]

    # 결과값을 갱신할 지 여부
    if window > result:
        result = window

print(result)
    