import sys
sys.stdin = open('input.txt')

h, w = map(int, input().split())
arr = list(map(int, input().split()))

tmp = arr[0]
for i in range(w):
    if arr[i] > h:
        arr[i] = h
height = max(arr)

# print(arr, '?')
# if height != w:
gap = 0
for i in range(w):
    if arr[i] < height:
        if tmp > arr[i]:
            gap += tmp - arr[i]
        elif tmp <= arr[i]:
            tmp = arr[i]
    else:
        tmp = height
        # height += gap
        # gap = 0
    # print(gap, '-', tmp, '-', arr[i])
# tmp = arr[-1]
# for j in range(w-2, height-1, -1):
#     # print(j, '?')
#     if tmp > arr[j]:
#         gap += tmp - arr[j]
#     elif tmp <= arr[j]:
#         tmp = arr[j]

        # print(gap, '-', tmp, '-', arr[j])
print(gap)

# print(arr)

# ------------------------------------------------------
h, w = map(int, input().split())
world = list(map(int, input().split()))

ans = 0
for i in range(1, w - 1):
    left_max = max(world[:i])
    right_max = max(world[i+1:])

    compare = min(left_max, right_max)

    if world[i] < compare:
        ans += compare - world[i]

print(ans)