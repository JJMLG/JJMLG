a = list(map(int, input().split()))
c = list(map(int, input().split()))
Blist = []
Blist.append(c[0] - a[2])
Blist.append(c[1] // a[1])
Blist.append(c[2] - a[0])
print(*Blist)