N=int(input())
numlist = list(map(str, range(1,N+1)))
result = 0
for i in numlist:
    result += i.count('3')+i.count('6')+i.count('9')
print(result)
