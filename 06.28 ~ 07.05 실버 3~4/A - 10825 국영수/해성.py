import sys
sys.stdin = open('input.txt')
N = int(input())
total = list(input().split() for _ in range(N))
for i in total:
    i[1], i[2], i[3] = int(i[1]), int(i[2]), int(i[3])
total.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))
for i in total:
    print(i[0])

# for i in range(len(total)):
#     for j in range(len(total)-i-1):
#         # 국어 젤 작은게 뒤로
#         if int(total[j][1]) < int(total[j+1][1]):
#             total[j], total[j+1] = total[j+1], total[j]
#         #     국어 같으면 영어 젤 큰게 뒤로
#         elif int(total[j][1]) == int(total[j+1][1]):
#             if total[j][2] > total[j + 1][2]:
#                 total[j], total[j + 1] = total[j+1], total[j]
#             # 국어도 같고 영어도 같으면
#             elif int(total[j][2]) == int(total[j+1][2]):
#                 # 수학 젤 작은게 뒤로
#                 if int(total[j][3]) < int(total[j+1][3]):
#                     total[j], total[j+1] = total[j+1], total[j]
#                 #     다 같으면 사전 순 증가
#                 elif int(total[j][3]) == int(total[j+1][3]):
#                     if ord(total[j][0][0]) > ord(total[j+1][0][0]):
#                         total[j], total[j + 1] = total[j + 1], total[j]
# for i in total:
#     print(i[0])
