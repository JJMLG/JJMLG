def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)

    return answer

    # 시간초과 코드
    # for i in range(len(numbers) - 1):
    #     if numbers[i] < numbers[i + 1]:
    #         answer.append(numbers[i + 1])
    #     else:
    #         num = numbers[i + 1:]
    #         maxx = 0
    #         for j in num:
    #             if numbers[i] < j:
    #                 maxx = j
    #                 break
    #
    #         if maxx != 0:
    #             answer.append(maxx)
    #         else:
    #             answer.append(-1)
    # answer.append(-1)
    return answer