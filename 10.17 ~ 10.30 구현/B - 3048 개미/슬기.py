import sys
sys.stdin = open('input.txt')

n1, n2 = map(int, input().split())
ant1 = list(input())    # 왼 -> 오
ant2 = list(input())    # 왼 <- 오
t = int(input())

new_ant1 = ant1[::-1]
ans = new_ant1 + ant2

for _ in range(t):
    for i in range(len(ans) - 1):
        if ans[i] in ant1 and ans[i+1] in ant2:
            ans[i], ans[i+1] = ans[i+1], ans[i]
            if ans[i+1] == new_ant1[-1]:
                break
print(''.join(ans))