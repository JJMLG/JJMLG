import sys

n,m = map(int,input().split())
ls_1 = set(map(int,input().split()))
ls_2 = set(map(int,input().split()))
cha = ls_1 & ls_2
cnt = len(cha)
print(n+m-cnt*2)
