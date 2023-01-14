import sys
sys.stdin = open('input.txt')

num, new = map(int, input().split())

new_num = str(new) + str(num)
# print(new_num)
arr = [True] * (int(new_num)+1)

for i in range(2, int(new_num)+1):
    if arr[i] == True:
        for j in range(i+i, int(new_num)+1, i):
            arr[j] = False

# print(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])
arr[0] = False
arr[1] = False
# print(arr)
if arr[int(new_num)] == True and arr[num] == True:
    print('Yes')
else:
    print('No')