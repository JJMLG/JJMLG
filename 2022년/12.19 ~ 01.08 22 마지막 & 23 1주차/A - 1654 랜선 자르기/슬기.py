import sys
sys.stdin = open('input.txt')

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]


def binary_search(lan):
    s = 1
    e = max(lan)

    while s <= e:
        mid = (s + e) // 2
        lines = 0

        for i in lan:
            # print(mid)
            lines += i // mid
            # print(lines)
        if lines >= n:
            s = mid + 1
        else:
            e = mid - 1

    return e

print(binary_search(lan))