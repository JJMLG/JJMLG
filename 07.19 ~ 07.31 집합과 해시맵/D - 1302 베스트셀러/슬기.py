import operator
import sys
sys.stdin = open('input.txt')

n = int(input())
not_duplicated = {}

for _ in range(n):
    book = input()
    if book not in not_duplicated:
        not_duplicated[book] = 1
    else:
        not_duplicated[book] += 1

best_sell = []
max_num = max(not_duplicated.values())


for i in not_duplicated:
    if max_num == not_duplicated[i]:
        best_sell.append(i)

best_sell.sort()
print(best_sell[0])