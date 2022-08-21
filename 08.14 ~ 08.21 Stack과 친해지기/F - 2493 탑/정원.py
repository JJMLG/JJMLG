import sys

input = sys.stdin.readline

N = int(input())
T = list(map(int, input().split())) # tower
S, result = [], [0] * N # stack
for i in range(N):
    t = T[i]
    while S and T[S[-1]] < t: S.pop() # 스택 정리
    if S: result[i] = S[-1] + 1
    S.append(i)
    for s in S: print(T[s], end=' ')
    print(S, result)
print(*result)

"""
스택에 들어있는, 현재 탑보다 낮은 탑의 인덱스를 전부 제거한다
스택이 남아있을 때, stack[-1]의 인덱스는
앞에서 등장했던 탑들 중 현재 탑 다음으로 높은 탑이 되고
레이저 신호는 여기서 수신될 것이다
현재 탑의 신호 수신탑에, stack[-1]+1번째 탑을 저장한다
그리고 해당 탑의 인덱스를 스택에 추가한다

늘 코드의 시작부터 적는 습관이 있었는데
위의 코드는 진행 중간만 깔끔하게 적혀있다
위 코드처럼 짤 수 있도록 더 열심히 해야겠다... ㅜㅜ
"""

# 쾅
# import sys

# input = sys.stdin.readline

# N = int(input())
# T = list(map(int, input().split())) # tower
# S = [] # stack
# result = [0] * N
# for i in range(N-1, -1, -1): # 진행은 우->좌 가 맞다
#     t = T[i]
#     if not S: 
#         S.append((t, i))
#     else:
#         S.append((t, i))
#         for j in range(len(S)-1, -1, -1):
#             if j < len(S)-1:
#                 if t > S[j][0]:
#                     result[S[j][1]] = i+1
#                     S.pop()
#                 else: pass
# print(*result)