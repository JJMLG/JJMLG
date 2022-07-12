import sys
sys.stdin=open('input.txt')
n = int(input())
a, b = map(int, input().split())
m = int(input())
family = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = []
res = [0] * (n+1)
for _ in range(n):
    try:
        parent, son = map(int, input().split())
        family[son].append(parent)
        family[parent].append(son)
    except:
        pass
def dfs(start):
    visited[start] = True
    for i in family[start]:
        if not visited[i]:
            res[i] = res[start] + 1
            dfs(i)
dfs(a)
if res[b]>0:
    print(res[b])
else:
    print(-1)
# -----------------------------------
# import sys
# import copy
# sys.stdin=open('input.txt')
# n = int(input())
# a, b = map(int, input().split())
# m = int(input())
# family = [ False for _ in range(n+1)]
# cnt = []
# result = []
# parent = 0
# for _ in range(n):
#     try:
#         parent, son = map(int, input().split())
#         family[son] = parent
#     except:
#         pass
#
# def dfs(start):
#     global cnt, parent
#     if family[start]==False:
#         parent = start
#         cnt.append(start)
#     else:
#         cnt.append(start)
#         dfs(family[start])
#     # return parent
#     return cnt
# dfs(a)
# result = cnt.copy()
# cnt =[]
# dfs(b)
# # print(cnt)
# # print(result)
# finalresult=0
# for i in range(len(cnt)):
#     for j in range(len(result)):
#         if cnt[i] == result[j]:
#             finalresult = len(cnt[:i])+ len(result[:j])
# if finalresult == 0:
#     if family[b] ==a:
#         print(1)
#     else:
#         print(-1)
# else:
#     print(finalresult)
#
# # if dfs(a) == dfs(b):
# #     print(cnt)
# # else:
# #     if dfs(a) == b:
# #         print(1)
# #     else:
# #         print(-1)