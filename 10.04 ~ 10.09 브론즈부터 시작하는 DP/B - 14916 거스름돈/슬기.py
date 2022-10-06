import sys
sys.stdin = open('input.txt')

n = int(input())

change = {2: 0, 5: 0}
# print(change)

dp = [2, 5]


while True:
    i = n
    print(i)
    if i == 1:
        print(-1)
        break

    elif i % 5 == 0:
        change[5] += 1
        i = i - 5

    elif i % 2 == 0:
        change[2] += 1
        i = i - 2

    elif i % 7 == 0:
        change[2] += 1
        change[5] += 1
        i = i - 7

    else:
        print(-1)
        # break

print(change)

