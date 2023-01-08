import sys
sys.setrecursionlimit(10**6)
n = int(input())
# 바보같이 아래처럼 n을 17로 맥시멈 잡아서 인덱스 오류 계속 남
# ans = [0 for _ in range(17+1)]
ans = [False for _ in range(n+1)]
# print(ans)
ans[1] =1
def nemo(n):
    if ans[n] != False:
        return ans[n]
    else:
        if n % 2 == 1:
            ans[n] = (2 * nemo(n-1)) - 1
            return ans[n]
        if n % 2 == 0:
            ans[n] = (2 * nemo(n-1)) + 1
            return ans[n]
nemo(n)

print(ans[n] % 10007)