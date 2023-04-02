def solution(ingredient):
    ls = [1,2,3,4,5,6]

    answer = 0
    stack = []
    for i in range(len(ingredient)):
        stack.append(ingredient[i])
        if stack and stack[-4:] == [1,2,3,1]:
            answer += 1
            for j in range(4):
                stack.pop()
    return answer
        