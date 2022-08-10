import sys

a,b,c = map(int,input().split())

ls = [0]*101
for _ in range(3):
    z,x = map(int,input().split())
    for i in range(z,x):
        ls[i] += 1


ans = 0
for i in range(len(ls)):
    if ls[i] == 1:
        ans += a*1
    elif ls[i] == 2:
        ans += b*2
    elif ls[i] == 3:
        ans += c*3

print(ans)

'''
12 분 47 초
'''