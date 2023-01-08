import sys
from itertools import combinations
from pprint import pprint

t = int(input())
for _ in range(t):
    dict = {}
    result = []
    n = int(input())
    ls_1 = list(map(int,input().split()))
    m = int(input())
    ls_2 = list(map(int,input().split()))

    for i in range(n):
        dict[ls_1[i]] = 1   
    
    for j in ls_2:
        if j in dict:
            
            print(1)
        else:
            print(0)

   