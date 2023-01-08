import sys

def find(x):
    real= 0
    arr = list(range(x, 2*x))
    for i in range(x):
        cnt =0
        for j in range(arr[i]):
            if j!=0 and j!=1 and j!= 123457 and arr[i]% j !=0:
                cnt +=1
        if cnt == j+1:
            real +=1
            arr[i]=123457

    return real


# x = input()
# print(x)
x = [input() for _ in range(8)]
# print(x)
for i in x:
    print(find(int(i)))
# x = list
# (map(int, input().split()))
# print(x)
