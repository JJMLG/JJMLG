import sys
sys.stdin = open('input.txt')

n = int(input())
card = sorted(list(map(int, input().split())))
m = int(input())
find_card = list(map(int, input().split()))

def binary(find, arr, left, right):
    if left > right:
        return 0

    mid = (left + right) // 2

    if arr[mid] == find:
        return arr[left:right+1].count(find)
    elif arr[mid] < find:
        return binary(find, arr, mid+1, right)
    else:
        return binary(find, arr, left, mid-1)

temp = {}
for i in card:
    if i not in temp:
        temp[i] = binary(i, card, 0, n-1)

print(' '.join(str(temp[x]) if x in temp else '0' for x in find_card ))

# for j in find_card:
#     if j in temp:
#         print(' '.join(str(temp[j])), end=' ')
#     else:
#         print('0', end=' ')