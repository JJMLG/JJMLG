from collections import deque
import sys

from itertools import combinations

n = int(input())
x = 2*n-1
y = (2*n-2)*2 +1

arr = [[" "]*(y) for _ in range(x)]
left = 0 
right = n-1
for i in range(n):
    for j in range(n):
  
        if i == 0:
            arr[i][j] = "*"
            arr[x-i-1][j] = "*"
            arr[i][y-j-1] = "*"
            arr[x-i-1][y-j-1] = "*"
        
        else:
            arr[i][left] = "*"
            arr[x-i-1][left] = "*"
            arr[i][y-left-1] = "*"
            arr[x-i-1][y-left-1] = "*"


            arr[i][right] = "*"
            arr[x-i-1][right] = "*"
            arr[i][y-right-1] = "*"
            arr[x-i-1][y-right-1] = "*"
            break

    left += 1
    right += 1
    

for i in range(x):
    ls = ""
    for j in range(y):
        ls += arr[i][j]
    print(ls.rstrip())
