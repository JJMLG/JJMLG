import sys
sys.stdin = open('input.txt')

n = int(input())
nums = list(map(int, input().split()))

start = 0
for i in range(n - 1, 0, -1):
    if nums[i - 1] < nums[i]:
        start = i - 1
        break
for i in range(n - 1, 0, -1):
    if nums[start] < nums[i]:
        nums[start], nums[i] = nums[i], nums[start]
        nums = nums[:start + 1] + sorted(nums[start + 1:])
        print(*nums)
        exit()
print(-1)