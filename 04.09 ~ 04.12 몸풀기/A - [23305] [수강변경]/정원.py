# N = int(input())
# student = []
# for i in list(map(int, input().split())):
#     student.append([i])
# j = 0
# for i in list(map(int, input().split())):
#     student[j].append(i)
#     j += 1
# for i in range(N):
#     for j in range(i, N):
#         if student[i][1] == student[j][0]:
#             student[i][0], student[j][0] = student[j][0], student[i][0]
#         elif student[j][1] == student[i][0]:
#             student[i][0], student[j][0] = student[j][0], student[i][0]
# result = 0
# for s in student:
#     if s[0] != s[1]:
#         result += 1
# print(result)

"""
원하는 학생들끼리 일대일로 교환시켜주는 코드를 짰는데
시간초과가 나왔다
문제는 "그래서 원하는 수업을 못 듣는 학생수는 몇명인가" 였고
아래 코드를 통하여 해결하였다
"""

# 핵심은 수업 교환횟수는 제한이 없고
# 학생들끼리 어떻게든 돌리고 돌리다 남는 학생의 수만 구하면 됨
N = int(input())
dp = [0] * 1000001 # 수업들 목록
for i in list(map(int, input().split())):
    dp[i] += 1 # 해당 수업을 신청하였음
result = 0 # 원하는 수업을 듣지 못하는 학생 수
for i in list(map(int, input().split())):
    if dp[i] >= 1: # 그 수업을 들고 있는 사람이 있으면
        dp[i] -= 1 # 교환
    else: # 그 수업을 들고 있는 사람 자체가 없으면
        result += 1 # 원하는 수업을 듣지 못하는 사람
print(result)