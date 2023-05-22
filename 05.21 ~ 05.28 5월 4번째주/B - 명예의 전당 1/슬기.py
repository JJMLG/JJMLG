def solution(k, score):
    answer = []

    stack = []
    for i in score:
        stack.append(i)
        stack.sort(reverse=True)
        if len(stack) > k:
            del stack[-1]
        answer.append(stack[-1])

    return answer