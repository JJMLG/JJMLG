def solution(numbers):
    N = len(numbers)
    stack = []
    ans = [-1] * N
    
    for i in range(N):
        while stack and numbers[stack[-1]] < numbers[i]:
            ans[stack.pop()] = numbers[i]
        stack.append(i)
    return ans

  
# def solution(numbers):
#     N = len(numbers)
#     ans = [-1] * N
#     for i in range(N - 1, -1, -1):
#         for j in range(i - 1, -1, -1):
#             if numbers[i] <= numbers[j]:break
#             ans[j] = numbers[i]
#     return ans
