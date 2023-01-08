import sys
sys.stdin = open('input.txt')


s = list(input())
t = list(input())

tmp = t
flag = 1
while True:
    if tmp == s:
        # print(tmp)
        flag = 0
        break

    # print(tmp)
    if len(tmp) > 0:
        if tmp[-1] == 'A':
            tmp = tmp[:-1]
        else:
            tmp = tmp[::-1]
            tmp = tmp[1:]
    else:
        break

if flag:
    print(0)
else:
    print(1)