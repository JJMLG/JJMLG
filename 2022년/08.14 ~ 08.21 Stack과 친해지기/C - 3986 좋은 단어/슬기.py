import sys
sys.stdin = open('input.txt')

n = int(input())

cnt = 0
for _ in range(n):
    word = input()
    stack = []

    for i in range(len(word)):
        if not stack:
            stack.append(word[i])
        else:
            if word[i] == stack[-1]:
                stack.pop()
                # cnt += 1
            else:
                stack.append(word[i])
    # print(stack)
    if not stack:
        cnt += 1

print(cnt)
