# solution_1
def binary(t, s, e): # target, start, end
    if s > e: return 0
    i = (s+e) // 2 # index
    if t == arr1[i]: return 1
    elif t < arr1[i]: return binary(t, s, i-1)
    elif t > arr1[i]: return binary(t, i+1, e)

N = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()
M = int(input())
arr2 = list(map(int, input().split()))
for a in arr2:
    s, e = 0, N-1
    print(binary(a, s, e))

# # solution_2
# N = int(input())
# arr1 = set(map(int, input().split()))
# M = int(input())
# arr2 = list(map(int, input().split()))
# for a in arr2:
#     if a in arr1: print(1)
#     else: print(0)