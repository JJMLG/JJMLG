import sys
sys.stdin = open('input.txt')

k = int(input())
inequality = input().split(' ')
num = list(range(0, 10))
# print(num)
# print(inequality)
small = num[:k+1]
big = num[:len(num)-(k+2):-1]
# print(big)
result = []
tmp = 0
minn = min(small)
maxx = max(small)
for i in inequality:
    for j in range(k):
        if i == '<':
            if small[j] <= tmp:
                continue
        else:
            if small[j] > small[j+1]:
                continue
            else:
                small[j], small[j+1] = small[j+1], small[j]
                print(small)

print(small)