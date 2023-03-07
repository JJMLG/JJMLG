import sys
sys.stdin = open('input.txt')

n = int(input())

num = []
for _ in range(n):
    word = input()
    tmp = ''

    for i in word:
        if i.isdigit():
            tmp += i
        else:
            if tmp:
                num.append(int(tmp))
                tmp = ''
            else:
                tmp = ''
    if tmp:
        num.append(int(tmp))

num.sort()
for i in num:
    print(i)