N, K, A, B = map(int, input().split())
water = [K] * N         # N개의 화분에 있는 수분
day = 0

while water[0]:         # 맨 앞에 제일 수준이 적은 화분이 온다
    for i in range(A):  # 물 주기
        water[i] += B
    for i in range(N):  # 물 감소
        water[i] -= 1
    water.sort()        # 가장 적은게 맨 앞으로 오게 정렬
    day += 1

print(day)
######################################################################################
N, K, A, B = map(int, input().split())
group = N // A              # A는 N의 약수니까 화분을 그룹으로 묶어서 그룹 단위로 본다
water = [K] * group         # 각 그룹에 있는 수분
idx = day = 0               # idx는 어느 그룹에 물을 줘야 하는지

while True:
    water[idx] += B         # 물 주기
    for i in range(group):  # 물 감소
        water[i] -= 1
    day += 1

    if min(water) == 0:
        break
    idx = (idx + 1) % group # 다음 물 줄 그룹의 idx

print(day)
######################################################################################
N, K, A, B = map(int, input().split())
day = 0
group = N // A              # 앞 그룹부터 차례로 물을 주면 가장 먼저 죽는건 마지막 그룹이다
                            # K를 마지막 그룹의 수분이라고 한다
while True:
    day += 1
    if day % group == 0:    # 마지막 그룹에 물을 줄 날짜이면
        K += B              # 물 주기
    K -= 1                  # 물 감소
    if K == 0:
        break

print(day)
