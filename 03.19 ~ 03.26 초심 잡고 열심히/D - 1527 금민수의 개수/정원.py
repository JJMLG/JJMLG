from collections import deque

A,B = map(int,input().split())
Q = deque()

Q.append(4); Q.append(7)
result = 0

while Q:
    GMS = Q.popleft()

    if GMS<=B:
        if A<=GMS: 
            result += 1 # A이상 B이하 만족하는 금민수
        Q.append(GMS*10+4) # 다음 금민수 1
        Q.append(GMS*10+7) # 다음 금민수 2

print(result)