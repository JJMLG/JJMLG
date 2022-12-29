import sys
sys.stdin = open('input.txt')



def binary_search(m1, m2):
    s = 0
    e = len(m1) - 1
    # print(m2, '?')
    while s <= e:
        mid = (s+e) // 2
        # print(mid, '???')
        if m1[mid] == m2:
            # print(mid, m2, m1[mid], 'mid')
            return 1

        if m1[mid] < m2:
            s = mid + 1
        else:
            e = mid - 1

    return 0


t = int(input())

for _ in range(t):
    n = int(input())
    memo_1 = list(map(int, input().split()))
    m = int(input())
    memo_2 = list(map(int, input().split()))

    memo_1.sort()
    for i in memo_2:
        print(binary_search(memo_1, i))



