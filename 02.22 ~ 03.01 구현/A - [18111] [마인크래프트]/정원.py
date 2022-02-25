import sys # 주어진 시간이 적은 문제
# sys.stdin.readline()과 PyPy3을 사용

N, M, B = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

time, height = 9223372036854775807, 0 # 가상의 최대시간, 높이

for h in range(257): # 브루트포스, 모든 높이에 대한 소요시간과 높이 계산
    # 동일 시간인 경우 더 높은 높이를 출력할 것이므로 
    # 높이는 0에서 256으로 진행

    bot = top = 0 # 변수 초기화

    # 매 높이 h에 대하여, 모든 배열 순회
    for i in range(N):
        for j in range(M):
            if arr[i][j] < h: # 블럭을 채워야하면
                bot += h-arr[i][j] # bot에 추가
            else: # 블럭을 깎아야하면
                top += arr[i][j]-h # top에 추가

    if bot > top + B: # 가진블럭 + 깎은블럭으로도 다 채우지 못하면
        continue # 지나가고

    t = bot + top*2 # 걸리는 시간은 채우기1초 깎기2초를 총 더한 시간

    if t <= time:
        time = t # 최소시간 갱신
        height = h # 최대높이 갱신

print(time, height) # 출력