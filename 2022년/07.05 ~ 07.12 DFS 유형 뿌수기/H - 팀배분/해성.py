import sys
sys.stdin = open("input.txt")
n = int(input())
hateInfo = [[] for _ in range(n+1)]
visited = 0 *(n+1)
for numb in range(n):
    temp = list(map(int, input().split()))
    for i in temp[1:]:
        hateInfo[numb+1].append(i)
teamOne = []
teamTwo = []
    for i in range(1, len(hateInfo)+1):
        teamOne[i]
print(hateInfo)
