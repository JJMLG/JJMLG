
import sys
from collections import deque
from pprint import pprint
sys.stdin = open('input.txt')


n,q = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(2**n)]
temp = [[0]*(2**n) for _ in range(2**n)]

print(temp)
def turn(size):
    # for k in range(0,8,2**size):
    #     print(k)
    for i in range(0,8,2**size):
        for j in range(0,8,2**size):
            # print(i,j)
            # temp[j][k+2**size-1-i] = arr[i][j]

            # 0 2 
            for q in range(i,i+2**size):
                for w in range(j,j+2**size):
                    temp[w][2**size-q-1] = arr[q][w]
    pprint(temp)
turn(1)
# print(arr)
