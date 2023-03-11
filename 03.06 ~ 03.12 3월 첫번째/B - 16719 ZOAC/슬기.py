import sys
sys.stdin = open('input.txt')

word = list(input())

res = [''] * len(word)

def dfs(s, arr):
    if not arr:
        return
    min_val = min(arr)
    # print(min_val)
    tmp = arr.index(min_val)

    res[s+tmp] = min_val
    # print(res)
    print(''.join(res))
    dfs(s+tmp+1, arr[tmp+1:])

    dfs(s, arr[:tmp])
dfs(0, word)