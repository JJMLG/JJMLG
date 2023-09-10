import sys
sys.stdin = open('input.txt')

N, kim, lim = map(int, input().split())
ans = 0
while True:
    kim = (kim + 1) // 2    # 다음 번호
    lim = (lim + 1) // 2    # 다음 번호
    ans += 1
    if kim == lim:          # 같으면 대결하는 것
        break
print(ans)
