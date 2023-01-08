import sys
N = int(input())
# ans는 기록
ans = [False] * (N+2)
# result = []
# a = 0
ans[1]=1
ans[2]=2
min_value = N+1
temp = 0
for i in range(int(N ** (1 / 2)) + 1):
    ans[i**2] = 1


for i in range(2, N+1):
    if ans[i] !=False:
        pass
    else:
        min_value = N +1
        # 제곱수만 돌려본다.
        x = list(range(1, int(i ** (1 / 2))+1))
        for j in x:
            temp = ans[i-(j**2)] + ans[j**2]
            if min_value >= temp:
                min_value = temp
                if min_value == 2:
                    ans[i] = 2
                    break
            else:
                pass
        ans[i] = min_value
print(ans[N])

