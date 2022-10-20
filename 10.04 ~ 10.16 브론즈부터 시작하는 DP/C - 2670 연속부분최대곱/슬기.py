import sys
sys.stdin = open('input.txt')

n = int(input())
nums = [float(input()) for _ in range(n)]

for i in range(1, n):
    nums[i] = max(nums[i], nums[i-1] * nums[i])
print('%0.3f' % max(nums))
