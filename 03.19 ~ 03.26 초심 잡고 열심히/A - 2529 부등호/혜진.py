k = int(input())
lst = input().split()
nums = [
    [str(i) for i in range(9, 9 - 1 - k, -1)],  # 최댓값 만들 때 쓰일 수
    [str(i) for i in range(k + 1)]              # 최솟값 만들 때 쓰일 수
]
used = [0] * (k + 1)
ans = ['', '']                  # 0: 최댓값, 1: 최솟값

def recur(idx, tmp, n):         # 문자의 길이, 문자, 최대인지 최소인지
    if ans[n]:                  # 만들어졌으면 그게 이미 최소이거나 최대니까 return
        return

    if idx > k:                 # 처음 만들어졌으면 그게 최소이거나 최대
        ans[n] = tmp
        return

    for i in range(k + 1):
        if used[i]: continue    # 중복 방지
        if idx == 0 or eval(tmp[-1] + lst[idx - 1] + nums[n][i]):   # 첫번째 숫자이거나 부등호가 성립한다
            used[i] = 1
            recur(idx + 1, tmp + nums[n][i], n)
            used[i] = 0

recur(0, '', 0)                 # 최댓값
recur(0, '', 1)                 # 최솟값
for a in ans:
    print(a)
