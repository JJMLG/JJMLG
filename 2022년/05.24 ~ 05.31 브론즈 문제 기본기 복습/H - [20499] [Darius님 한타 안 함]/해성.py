KDA = list(map(int,(input().split('/'))))
# print(KDA)
if KDA[0]+KDA[2] < KDA[1] or KDA[1] ==0:
    print("hasu")
else:
    print("gosu")