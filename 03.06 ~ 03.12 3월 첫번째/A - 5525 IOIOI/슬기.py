import sys
sys.stdin = open('input.txt')


n = int(input())
m = int(input())
s = input()

cnt = 0
tmp = 0

i = 1

while i < m-1:
    if s[i-1] == 'I' and s[i] == 'O' and s[i+1] == 'I':
        tmp += 1
        if tmp == n:
            tmp -= 1
            cnt += 1
        i += 1
    else:
        tmp = 0
    i += 1

print(cnt)