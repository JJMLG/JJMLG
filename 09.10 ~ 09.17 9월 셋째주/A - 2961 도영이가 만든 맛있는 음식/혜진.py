N = int(input())
taste = [tuple(map(int, input().split())) for _ in range(N)]
ans = 1000000000

def recur(si, sour, bitter):
    global ans
    ans = min(ans, abs(sour - bitter))

    if ans == 0 or si == N:
        return
    
    for i in range(si, N):
        recur(i + 1, sour * taste[i][0], bitter + taste[i][1])

for i in range(N):
    recur(i + 1, taste[i][0], taste[i][1])

print(ans)


# from itertools import combinations as cb
# N = int(input())
# taste = [tuple(map(int, input().split())) for _ in range(N)]
# ans = 1000000000
# for n in range(1, N + 1):
#     recipes = cb(range(N), n)
#     # print(list(recipes))
#     for recipe in recipes:
#         sour = 1
#         bitter = 0
#         for rec in recipe:
#             # print(rec, end=' ')
#             sour *= taste[rec][0]
#             bitter += taste[rec][1]
#         ans = min(ans, abs(sour - bitter))
#         # print()
# print(ans)

