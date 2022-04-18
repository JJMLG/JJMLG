import sys
sys.stdin=open('10819.txt')
N = int(input())
numlist = list(map(int, input().split()))

maxsum = 0
templist = []
tempsum =0
visited = [0] * N
# result =[ ]
# 1~6까지 조합 한다음 순서대로 계산해보기
# 그담 최대값을 교체해주기
def dfs(x):
    global maxsum
    if len(templist)==N:
        start = 0
        tempsum = 0
        while start < N-1:
            tempsum += abs(templist[start] - templist[start+1])
            start += 1
        if tempsum > maxsum:
            maxsum = tempsum
        else:
            pass
    else:
        for i in range(N):
            if visited[i] == 1:
                pass
            else:
                visited[i] = 1
                templist.append(numlist[i])
                dfs(x+1)
                visited[i] = 0
                templist.pop()
    return maxsum
print(dfs(0))
