def solution(number, k):
    answer = ''

    #     순서는 지켜야 함
    stack = []
    flag = 0
    for i in number:
        while stack and stack[-1] < i:
            if flag != k:
                stack.pop()
                flag += 1
            else:
                break
        stack.append(i)

    while flag < k:
        stack.pop()
        flag += 1
    # print(stack)

    for i in stack:
        answer += i
    # print(*stack, sep="")
    #     arr = []
    #     def recur(cur, start):
    #         if cur == len(number) - k:
    #             print(arr)
    #             return

    #         for i in range(start, len(number)):
    #             arr.append(number[i])
    #             recur(cur+1, i + 1)
    #             arr.pop()

    #     recur(0, 0)

    return answer