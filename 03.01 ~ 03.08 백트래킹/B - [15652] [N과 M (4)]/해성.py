import sys
sys.stdin = open("15652.txt")

N, M = map(int, input().split())
result = []
temp = []

def backtrack(temp):
    if len(temp) >= M:
        print(' '.join(map(str, temp)))
        # result.append(temp.copy())
    else:
        for i in range(1, N+1):
            if len(temp) == 0:
                temp.append(i)
                backtrack(temp)
                temp.pop()
            else:
                if temp[-1] > i:
                    pass
                else:
                    temp.append(i)
                    backtrack(temp)
                    temp.pop()
    return result
backtrack(temp)
