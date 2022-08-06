import sys
sys.stdin = open('input.txt')


def binary(find):
    left = 0
    right = n-1

    while left <= right:
        mid = (left + right) // 2

        if memo1[mid] == find:
            return True

        if memo1[mid] < find:
            left = mid + 1

        elif memo1[mid] > find:
            right = mid - 1

t = int(input())

for _ in range(t):
    n = int(input())
    memo1 = sorted(list(map(int, input().split())))
    m = int(input())
    memo2 = list(map(int, input().split()))

    for i in range(m):
        if binary(memo2[i]):
            print(1)
        else:
            print(0)