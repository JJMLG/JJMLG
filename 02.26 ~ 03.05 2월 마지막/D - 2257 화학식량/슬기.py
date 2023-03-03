import sys
sys.stdin = open('input.txt')

n = input().split('(')
# nn = n.
print(n)

ori = ''
tmp = ''
stack = []
flag = 0

print(stack)
print(tmp)
cnt = 0
for i in stack:
    if i == 'H':
        cnt += 1
    elif i == 'C':
        cnt += 12
    else:
        cnt += 16
print(cnt)
