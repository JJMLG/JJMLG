import sys

cnt = 0
n,m = map(int,input().split())
dict = {}
for i in range(n):
    line, plat = map(int,input().split())
    if line not in dict:
        dict[line] = []
        dict[line].append(plat)
    else:
        dict[line].append(plat)

cnt = 0
for j in dict:
    stack = []
    
    for k in range(len(dict[j])):
        trash = 0
        if stack:
            while stack and dict[j][k] <= stack[-1]:
                if dict[j][k] == stack[-1]:
                    trash = stack.pop()
                else:
                    trash = stack.pop()
                    cnt += 1
        
            
        
        if dict[j][k] != trash:
            stack.append(dict[j][k])
            cnt +=1 
        else:
            stack.append(dict[j][k])
     
    
print(cnt)