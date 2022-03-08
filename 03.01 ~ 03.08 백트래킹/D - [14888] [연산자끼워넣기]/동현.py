import sys, itertools

input = sys.stdin.readline
n = int(input())
ls = list(map(int,input().split()))
yeon = list(map(int,input().split()))
a = ls[:]
yeonls= []





for i in range(yeon[0]):
    yeonls.append('+')
for i in range(yeon[1]):
    yeonls.append('-')
for i in range(yeon[2]):
    yeonls.append('*')
for i in range(yeon[3]):
    yeonls.append('/')



yeonlss = list(itertools.permutations(yeonls,len(yeonls)))

cal = 0
ans = []
for k in range(len(yeonlss)):
    i = 0
    ls = a[:]
    while True:
        if i == len(yeonlss[k]):
            break
        if yeonlss[k][i] == '+':
            ls[i+1] = ls[i]+ls[i+1]

        elif yeonlss[k][i] == '-':
            ls[i+1] = ls[i] - ls[i+1]

        elif yeonlss[k][i] == '*':
            ls[i+1] = ls[i] * ls[i+1]

        elif yeonlss[k][i] == '/':
            if ls[i] < 0:
                # if ls[i] // ls[i+1] == 0:
                #     ls[i+1] = 0
                #     continue
                ls[i+1] = -(-ls[i] // ls[i+1])
                i+=1
                continue
            ls[i+1] = ls[i] // ls[i+1]
        i += 1
    ans.append(ls[-1])

print(max(ans),min(ans), sep='\n')
