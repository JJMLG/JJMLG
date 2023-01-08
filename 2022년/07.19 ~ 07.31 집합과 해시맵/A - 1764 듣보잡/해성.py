N,M = map(int, input().split())
No=[]
result = []
sum=0
No = list(input() for _ in range(N+M))
No.sort()
for i in range(N+M-1):
    if (No[i] == No[i+1]):
        sum+=1
        result.append(No[i])
print(sum)
for i in range(sum):
    print(result[i])
