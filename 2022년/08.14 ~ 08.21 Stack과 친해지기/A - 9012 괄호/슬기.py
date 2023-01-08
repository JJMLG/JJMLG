import sys
sys.stdin = open('input.txt')

t = int(input())

for _ in range(t):
    stack = []
    parenthesis = input()
    # print(parenthesis)

    for i in parenthesis:
        if not stack:
            stack.append(i)
        else:
            if i == '(':
                stack.append(i)
            elif i == ')':
                # print(stack, '23213')
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(i)
    # print(stack)

    if not stack:
        # print(stack)
        print('YES')
    else:
        print('NO')