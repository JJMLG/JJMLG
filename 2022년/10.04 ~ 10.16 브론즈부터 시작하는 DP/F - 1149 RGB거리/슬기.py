import sys
sys.stdin = open('input.txt')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


color = []

for i in range(len(arr)):
    for j in range(len(arr[i])):
        pass


"""
1번 예
26
57
13

>> 6일 때
5
64
19
4
84
32
"""