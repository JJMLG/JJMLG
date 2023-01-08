N = int(input())
dct = {input(): i for i in range(N)} # 터널에 들어간 순서
result = 0
check = [0] * N # 나간 차 기록 list
for n in range(N): # 나가는 차 입력
    tmp = input() # 나간 차 번호판
    IN = dct[tmp] # 나간 차의 터널에 들어간 순서
    OUT = sum(check[:IN]) # 먼저 나간 차량 수
    # 내 앞 차량들의 수가 터널을 들어갈 때 보다 나올 때 더 적으면
    if OUT < IN: result += 1 # 추월차량
    check[IN] = 1 # 해당 차는 터널을 빠져나옴
print(result)