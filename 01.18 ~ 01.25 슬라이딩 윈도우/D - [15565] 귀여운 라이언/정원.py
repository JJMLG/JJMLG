N, K = map(int, input().split())

# 라이언 혹은 어피치
ryans = list(map(int, input().split()))

s = e = cnt = 0 # 시작 끝 라이언개수

if ryans[s] == 1: # 라이언으로 시작하면
    cnt += 1 # cnt 1로 초기화

result = N # 가상의 최대값

is_answer = False # 조합을 찾았는가??

while True: # 무지성 while True
    # while 종료 조건문
    # 1. 라이언이 K개 미만인데 더 뒤로 못 감
    # 2. 라이언이 K개 초과인데 더 앞에서 땡길 수 없음
    if (cnt < K and e == N-1) or (cnt > K and s == N-1):
        break

    if cnt == K: # K개 라이언인 구간 발견!
        if not is_answer: # 처음 발견한거면
            # K개인 라이언구간이 존재하니
            # 일단 답이 -1은 아님
            is_answer = True # 라이언구간 존재함 체크
        
        length = e-s+1 # 라이언구간의 길이
        if length < result: # 더 짧은 구간길이라면
            result = length # 최소 길이 갱신
        
        # 포인터를 옮길건데
        if ryans[s] == 1: # 구간 맨 앞이 라이언이면
            cnt -= 1 # 라이언 카운트 빼주고
        s += 1 # 한 칸 땡기기

    elif cnt < K: # K개 미만 라이언구간이면
        e += 1 # 한 칸 밀고
        if ryans[e] == 1: # 밀은 위치가 라이언이면
            cnt += 1 # 카운트

    elif cnt > K: # K개 초과 라이언구간이면
        if ryans[s] == 1: # 맨 앞이 라이언이면
            cnt -= 1 # 카운트 감소하고
        s += 1 # 한 칸 땡김

if is_answer: # K개인 라이언구간을 찾았었으면
    print(result)
else: # 못찾았었으면
    print(-1)