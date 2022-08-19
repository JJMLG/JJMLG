import sys
sys.stdin = open('input.txt')

stick = input()
# print(stick)
stack = []

result = 0
for i in range(len(stick)):
    if stick[i] == '(':
        stack.append('(')
    else:
        if stick[i-1] == '(':
            stack.pop()
            result += len(stack)

        else:
            stack.pop()
            result += 1

print(result)