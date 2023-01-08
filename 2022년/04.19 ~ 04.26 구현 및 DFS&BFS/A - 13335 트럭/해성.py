n, w, L = map(int, input().split())
TruckWeight = list(map(int, input().split()))
# 다리길이는 w만큼
Bridge = [False] * w
# 리스트 길이를 정해놓고 하나씩 위치를 인데스 0쪽으로 바꿔나가는데
# 문제는 들어가 있는 트럭들의 총 무게가 한계점보다 크다면 일단 넣지 않고 지금 넣을 트럭을 합쳤을 때 총무게보다 작을 때까지 기다림
countTime = 0
# A.일단 다리위에 누가 있으면 걔부터 앞으로 이동시키고
# 1-1 맨 앞에 누가 있는지 체크해서 있으면 내보내기 위해 빼고 0으로 바꿔주고
# 1-2 맨 앞이 아니면 앞으로 자리 바꿔주고
# 1-3 이제 올리려고하는데 다리길이가 꽉찼으면 올리면 안되고 끝내고
# 1-4 무게도 제한무게보다 크면 안되니까 그냥 끝내고
# 1-5 다리길이도 꽉 안찼고 무게도 제한무게보다 작다면 올린다.
# B. 누가 없으면 다리위에 올리기.
if n ==1:
    countTime = w+1
    print(countTime)
else:
    while TruckWeight:
        if len(TruckWeight)==0 and sum(Bridge)==0:
            print(countTime)
            break
        # 일단 트럭 빼야할 거 빼기
        nowTruck = TruckWeight.pop(0)
        # 누가 다리위에 있으면
        if sum(Bridge)>0:
            # 다리위 맨 앞에 누가 있으면 빼준다 == 걍 False로 바꿔줌
            if Bridge[0] != False:
                Bridge[0] = False
            if sum(Bridge)!=0:
            # 1-2 맨 앞이 아니면 안에 것들 앞으로 자리 바꿔주고
                for i in range(w-1):
                    Bridge[i] = Bridge[i+1]
            # 다리 맨뒤 체크안했으니 False로 바꿔주고
            Bridge[w-1] = False
            # 1-4 무게도 제한무게보다 크면 안되니까 그냥 끝내고
            # 1-5 다리길이도 꽉 안찼고 무게도 제한무게보다 작다면 올린다.
            if False in Bridge and sum(Bridge)+ nowTruck <=L:
                Bridge[w-1] = nowTruck
            else:
                TruckWeight.insert(0,nowTruck)        #
        # 누가 다리위에 없으면 일단 올리기
        else:
            Bridge[w-1] = nowTruck
        countTime+=1
    # 문제는 while문을 Bridge에 남은게 있으면도 하고 싶은데 그걸 못하노...
    # 그래서 Bridge에 False가 아닌게 남아있으면 없어질때까지 카운트세줌
    if sum(Bridge)>0:
        while sum(Bridge)>0:
            for i in range(w - 1):
                Bridge[i] = Bridge[i + 1]
            Bridge[w-1] = False
            countTime+=1
    print(countTime)

    # print(countTime)
