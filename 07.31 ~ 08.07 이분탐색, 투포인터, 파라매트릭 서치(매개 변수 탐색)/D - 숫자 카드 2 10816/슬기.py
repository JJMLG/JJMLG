import sys
sys.stdin = open('input.txt')

n = int(input())
card = sorted(list(map(int, input().split())))
m = int(input())
find_card = list(map(int, input().split()))

def binary(k, arr, left, right):
    if left > right:
        return 0

    mid = (left + right) // 2

    if k == arr[mid]:
        a, b = 1, 1
        while mid - a >= left:
            if arr[mid-a] != arr[mid]:
                break
            else:
                a += 1

        while mid + b <= right:
            if arr[mid+b] != arr[mid]:
                break
            else:
                b += 1
        return a + b -1

    elif k < arr[mid]:
        return binary(k, arr, left, mid-1)
    else:
        return binary(k, arr, mid+1, right)




temp = {}
for i in card:
    left = 0
    right = len(card) - 1
    if i not in temp:
        temp[i] = binary(i, card, left, right)
print(' '.join(str(temp[x]) if x in temp else '0' for x in find_card))
