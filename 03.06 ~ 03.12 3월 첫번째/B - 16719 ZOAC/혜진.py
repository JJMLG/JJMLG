origin = list(input())
ans = [''] * len(origin)

def func(startIdx, arr):
    if not arr:
        return

    minV = min(arr)
    minIdx = arr.index(minV)

    ans[startIdx + minIdx] = minV                   # 원래 위치에 넣어준다
    print(''.join(ans))

    func(startIdx + minIdx + 1, arr[minIdx + 1:])   # 오른쪽
    func(startIdx, arr[:minIdx])                    # 왼쪽

func(0, origin)
