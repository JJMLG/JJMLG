def calc(string):
    lst = list(map(int, string.split('+')))
    return sum(lst)

string = input()                # 최소값은 빼는 숫자가 커야하니까
lst = string.split('-')         # -를 기준으로 나눠서 다 더해서 뺀다

ans = 0
for i in range(len(lst)):
    if i == 0:                  # 첫번째 수는 더하고
        ans += calc(lst[i])
    else:                       # 나버지 수는 뺀다
        ans -= calc(lst[i])
print(ans)
