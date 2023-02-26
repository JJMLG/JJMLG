import sys
sys.stdin = open('input.txt')

n = input()
# print(n)

res = 0
tmp = []
tmp_2 = ''
flag = 0
for i in range(len(n)):
    temp = 0
    if n[i] == '-' or n[i] == '+':
        tmp.append(tmp_2)
        tmp_2 = ''
    tmp_2 += n[i]
if tmp_2:
    tmp.append(tmp_2)
print(tmp)