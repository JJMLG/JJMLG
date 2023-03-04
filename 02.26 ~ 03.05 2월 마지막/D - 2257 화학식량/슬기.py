import sys
sys.stdin = open('input.txt')

n = list(input())
print(n)

tmp = ''
tmp_2 = ''
stack = []
flag = 0
for i in range(len(n)):
    if n[i] == '(':
        continue
    elif n[i] == ')':
        stack.pop()
print(tmp)
print(tmp_2)
print(stack)