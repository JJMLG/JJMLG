import sys
sys.stdin = open('input.txt')

a, b, c = map(int, input().split())

park = {}

for _ in range(3):
    arrived, leave = map(int, input().split())
    time = list(range(arrived, leave))

    for i in time:
        if i not in park:
            park[i] = 1
        else:
            park[i] += 1
# print(park)
result = 0
for j in park.values():
    # print(j)
    if j <= 1:
        result += j * a
    elif j == 2:
        result += j * b
    elif j >= 3:
        result += j * c

print(result)


# 26분 걸림