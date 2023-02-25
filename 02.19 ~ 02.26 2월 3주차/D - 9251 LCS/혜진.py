A = input()
B = input()
a, b = len(A), len(B)

arr = [[0] * (a + 1) for _ in range(b + 1)]

for r in range(1, b + 1):
    for c in range(1, a + 1):
        if A[c - 1] == B[r - 1]:
            arr[r][c] = arr[r - 1][c - 1] + 1
        else:
            arr[r][c] = max(arr[r][c-1], arr[r-1][c])

print(arr[b][a])
