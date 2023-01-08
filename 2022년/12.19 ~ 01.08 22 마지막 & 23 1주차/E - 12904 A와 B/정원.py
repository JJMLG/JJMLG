S = list(input())
T = list(input())
result = 0
while len(T) > 0:
    if S == T: 
        result = 1
        break
    flag = False
    if T[-1] == 'B':
        flag = True
    T.pop()
    if flag:
        T = T[::-1]    
print(result)