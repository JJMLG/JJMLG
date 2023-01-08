import sys
sys.stdin=open('14889.txt')

N = int(input())
infos = [list(map(int, input().split())) for _ in range(N)]
    # for j in range(N):
# print(totals)
# print(infos)
visited=[0] * (N)
maxim = 200*N*N
sumTotal = 0
temp = 0
A=[]
B=[]
result = []
# visited = [0] * N
def maketeam(A):
    if len(A) == N//2:
        if sorted(A) in result:
            pass
        else:
            result.append(A.copy())
            B = []
            for i in list(range(N)):
                if i in A:
                    pass
                else:
                    B.append(i)
            # result.append(B)
    else:
        for i in range(N):
            if i in A:
                pass
            else:
                # visited[i] = 1
                A.append(i)
                maketeam(A)
                A.pop()
                # B.pop()
                # visited[i] =0
    return result
# print(maketeam(A))
maketeam(A)

def checkteam(i):
    if len(checktemp) == 2:
        checkresult.append(checktemp.copy())
    else:
        for j in i:
            if j in checktemp:
                pass
            else:
                # visited[i] = 1
                checktemp.append(j)
                checkteam(i)
                checktemp.pop()
                # visited[i] =0
    return checkresult

# for i in result:
final = 0
print(result)
# for i in result:
#     checktemp = []
#     checkresult = []
#     # print(checkteam(i))
#     for i in checkteam(i):
#         print(i)
#         # print()
#         final += infos[i[0]][i[1]]
#         print(final)
#         if final > maxim:
#             break
#     if  < maxim:
#         maxim =
# print(maxim)
    # print()

    # print(checkteam(i))
    # for i in checkteam(i):
    #     print(i)
    # print()
    # print()
    # for i in checkresult:
        # print(i)




# print(final)
    # print(final)


# def maketeam(A):
#     global temp
#     global sumTotal
#     #A팀의 인원이 차면
#     if len(A) == N//2:
#         # 하나씩 더해보기
#         for i in range(len(A)):
#             for j in range(len(A)):
#                 if i == j:
#                     pass
#                 else:
#                     temp += infos[A[i]][A[j]]
#         # 다른 팀원들과 값 계산해보기
#         # 전체 값
#         for x in range(N):
#             sumTotal+= sum([x])
#         if sumTotal> temp:
#             sumTotal =temp
#         # sumA = temp
#         # and len(B) == N // 2:
#         # if maxim < result:
#         #     maxim = result
#     else:
#         for z in (0, N):
#             if visited[z] == 1:
#                 pass
#             else:
#                 visited[z] = 1
#                 A.append(z)
#                 maketeam(A)
#                 A.pop(z)
#     return sumTotal
# maketeam(A)

