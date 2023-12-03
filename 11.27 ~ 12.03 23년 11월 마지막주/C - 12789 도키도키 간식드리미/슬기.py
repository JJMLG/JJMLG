import sys
sys.stdin = open('input.txt')

n = int(input())
num = list(map(int, input().split()))
cnt = 1
stack = []

while num:
    if cnt == num[0]:
        cnt += 1
        num.pop(0)
    else:
        stack.append(num.pop(0))

    while stack:
        if stack[-1] == cnt:
            stack.pop()
            cnt += 1
        else:
            break

if len(stack) == 0:
    print("Nice")
else:
    print("Sad")