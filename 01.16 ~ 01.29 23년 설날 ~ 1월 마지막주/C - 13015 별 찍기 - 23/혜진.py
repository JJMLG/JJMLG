N = int(input())

# 첫줄
print('*' * N + ' ' * (2 * (N - 1) - 1) + '*' * N)

arr = []
tmp = '*' + ' ' * (N - 2) + '*'

for i in range(1, N - 1):
    arr.append(' ' * i + tmp + ' ' * (2 * (N - 1 - i) - 1) + tmp)
    print(arr[i - 1])

# 한가운데
print(' ' * (N - 1) + tmp + ' ' * (N - 2) + '*')

L = len(arr)
for i in range(L):
    print(arr[L - i - 1])

# 막줄
print('*' * N + ' ' * (2 * (N - 1) - 1) + '*' * N)
