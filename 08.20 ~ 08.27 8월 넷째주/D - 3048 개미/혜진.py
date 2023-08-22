import sys
sys.stdin = open('input.txt')

n1, n2 = map(int, input().split())
ant1 = input()      # 첫 번째 그룹
ant2 = input()      # 두 번째 그룹
T = int(input())

arr = list(ant1)
arr.reverse()
arr += list(ant2)   # 전체 개미들 순서

def go(arr, R, L):  # 개미들 전진
    i = 0
    while i < len(arr) - 1:
        if arr[i] in R and arr[i + 1] in L:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i += 1
        i += 1
    return arr

for _ in range(T):
    arr = go(arr, ant1, ant2)

print(''.join(arr))