import sys
from collections import deque
import copy 

num = 1
while True:
    n = int(input())
    if n == 0:
        break
    dict = {}
    dict_2 = {}
    cnt = 0
    
    
    for i in range(n):
        a = input().split(' ')
    
        dict[a[0]] = a[1]
        dict_2[a[0]] = 1
    

    for name in dict:
        queue = deque()
        if dict_2[name] == 1:
            queue.append(name)
            flag =0 
            while queue:
                t = queue.popleft()
                if dict_2[t] == 0:
                    flag = 1
                    break

                queue.append(dict[t])
                dict_2[t] = 0
        
            if flag == 1:
                cnt +=1 

    print(num,cnt)
    num += 1