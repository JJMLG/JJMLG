import sys
sys.stdin = open('input.txt')

n = int(input())
card = list(map(int, input().split()))
m = int(input())
mine = list(map(int, input().split()))

card_dict = {}
for i in card:
    if i in card_dict:
        card_dict[i] += 1
    else:
        card_dict[i] = 1
# print(card_dict)

result = []
for j in mine:
    if j in card_dict:
        result.append(card_dict.get(j))
    else:
        result.append(0)
print(*result)