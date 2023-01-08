import sys


# 백트래킹 (브루트포스)로 만들 수 있는 숫자조합을 다 만드는 로직
# 같은 수가 중복되도 상관 없기 때문에 재귀 부분에 아무런 제약이 없음
# 근데 가장 큰 수가 1000임 (50*20) 
# 그렇기 때문에 빈 리스트를 초기화 시켜서 depth 조건이 충족될 때마다 자릿수를
# 1로 만들어서 체크함.
# 결국 초기화된 리스트의 sum이 서로 다른 숫자의 개수가 됨.
n = int(input())
rome = [1,5,10,50]
ls = []
sum_ls = [0] * 1001

def dfs(depth,num):

    if depth == n:
        sum_ls[sum(ls)] =1
        return

    for i in range(num,4):
        ls.append(rome[i])
        dfs(depth +1, i)
        ls.pop()


dfs(0,0)
print(sum(sum_ls))