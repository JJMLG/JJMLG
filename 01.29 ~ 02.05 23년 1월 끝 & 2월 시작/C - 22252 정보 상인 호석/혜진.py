from heapq import heapify, heappop

seller = {}
cost = 0

for _ in range(int(input())):
    n, name, m, *lst = input().split()
    if n == '1':
        tmp = list(map(lambda x: -int(x), lst))     # heapq는 작은 수가 앞으로 오니까 큰수를 앞으로 오게 하기 위해 음수로 바꾼다
        seller[name] = seller.get(name, []) + tmp
        continue
    try:                                            # 없는 정보상이면 except로 넘어간다
        if len(seller[name]) <= int(m):
            cost -= sum(seller[name])               # 음수로 바뀐 값들이니까 양수로 바꾸기 위해서 - 한다
            seller[name] = []
        else:
            heapify(seller[name])
            for _ in range(int(m)):
                cost -= heappop(seller[name])
    except: pass

print(cost)
