def delete_check(arr):
    if len(arr) >= 2 and arr[-1] == arr[-2]:
        for _ in range(2): arr.pop()

def solution(s):
    stack = []
    for i in s:
        stack.append(i)
        delete_check(stack)
    delete_check(stack)

    return 0 if stack else 1