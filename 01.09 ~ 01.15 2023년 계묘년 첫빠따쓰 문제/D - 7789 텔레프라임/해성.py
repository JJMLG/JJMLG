import sys
import math
sys.stdin = open("input.txt")

ordNumber,newNumber = input().split(" ")
newNumber= int(newNumber+ordNumber)
ordNumber = int(ordNumber)
arr = [0 for _ in range(newNumber+1)]
for i in range(2, int(math.sqrt(newNumber))+1):
    if(arr[i]):
        continue
    for j in range(2*i,newNumber+1,i):
        if(arr[j]):
            continue
        arr[j] = 1
if (arr[ordNumber] or arr[newNumber]):
    print("No")
else:
    print("Yes")
