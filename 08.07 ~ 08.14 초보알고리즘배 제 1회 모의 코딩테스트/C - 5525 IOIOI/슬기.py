import sys
sys.stdin = open('input.txt')

n = int(input())
m = int(input())
s = input()


p = 'I'
for _ in range(n):
    p += 'OI'
# print(p)

cnt = 0
for i in range(m):
    if s[i] == 'I':
        if s[i:len(p)+i] == p:
            cnt += 1
print(cnt)