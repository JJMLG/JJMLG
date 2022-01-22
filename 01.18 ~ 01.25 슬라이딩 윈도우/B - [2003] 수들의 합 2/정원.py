N, M = map(int, input().split())

seq = list(map(int, input().split())) # 수열 입력

s = e = 0 # 두포인터

now = sum(seq[s:e+1]) # 초기값(seq[0])

result = 0 # 크기가 M과 같은 수열 부분합의 개수 초기화

while True: # 무지성 while True
    # 종료조건
    # 1. e를 뒤로 밀어봤자 M보다 크거나 같아질 수 없음
    # 2. s를 뒤로 땡겨봤자 M보다 작거나 같아질 수 없음
    if (now < M and e == N-1) or (now > M and s == N-1):
        break

    if now == M: # 수열 부분합이 M과 같으면
        result += 1
        now -= seq[s]
        s += 1 # 앞에서 한 칸 땡기기
    elif now < M: # 부분합이 M보다 작으면
        e += 1 # 뒤로 한 칸 밀기
        now += seq[e]
    elif now > M: # 부분합이 M보다 크면
        now -= seq[s]
        s += 1 # 앞에서 한 칸 땡기기

print(result)