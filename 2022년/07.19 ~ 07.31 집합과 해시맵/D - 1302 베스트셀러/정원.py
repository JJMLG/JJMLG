N = int(input())
arr = dict()
for n in range(N):
    book = input()
    if book not in arr:
        arr[book] = 1
    else: # book in arr
        arr[book] += 1
result = [(a, arr[a]) for a in arr]
result.sort(key=lambda x:(-x[1], x[0]))
print(result[0][0])