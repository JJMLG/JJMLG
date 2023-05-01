from collections import deque
def solution(n):
    ans = 0
    
    while n:
        if n % 2 == 1:
            ans += 1
            n -= 1
        n = n//2
        

    return ans






# 시간초과
# def solution(n):
#     ans = 0
#     queue = deque()
    
#     queue.append(1)
#     visited = [0]*(n+1)
#     visited[1] = 1
#     while queue:
#         t = queue.popleft()
#         if t == n:
#             return visited
#         if t+1 < n+1:
#             if visited[t+1] == 0 or visited[t+1] > visited[t] + 1:
#                 queue.append(t+1)
#                 visited[t+1] = visited[t] + 1
#         if t*2 < n+1:
#             if visited[t*2] == 0 or visited[t*2] > visited[t]:
#                 queue.append(t*2)
#                 visited[t*2] = visited[t]
    
    
#     return ans