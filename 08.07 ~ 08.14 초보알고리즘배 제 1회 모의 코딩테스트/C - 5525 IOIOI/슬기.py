import sys
sys.stdin = open('input.txt')

n = int(input())
m = int(input())
s = input()
# s = list(input())
# print(s)

p = 'I'
for _ in range(n):
    # p.append('O')
    # p.append('I')
    p += 'OI'
# print(p)

cnt = 0
for i in range(m):
    if s[i] == 'I':
        # print(s[i:len(p)+i])
        if s[i:len(p)+i] == p:
            cnt += 1
print(cnt)