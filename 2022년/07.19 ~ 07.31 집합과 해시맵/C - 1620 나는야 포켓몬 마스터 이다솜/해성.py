N, M = map(int ,input().split())
dogam =dict()
Indexdogam =dict()
poke =''
temp =0
poke = [input() for i in range(N)]
for i in range(N):
    dogam[i] = poke[i]
    Indexdogam[poke[i]] = i
    # print(dogam)
temp = [input() for i in range(M)]
for i in range(M):
    if (temp[i].isdigit()==0):
        print(Indexdogam[temp[i]]+1)
    elif temp[i].isdigit():
        print(dogam[int(temp[i])-1])