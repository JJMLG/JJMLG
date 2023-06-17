from collections import deque


def solution(keymap, targets):
    answer = []

    def find(x):
        cnt = 0
        q = deque()
        q.append(x)

        while q:
            t = q.popleft()

            for k, v in arr.items():
                if t in v:
                    cnt += k
                    break

        return cnt

    arr = {}    # 해당 문자 담아줄 dic {0: 'A'}
    tmp = set()  # 중복 문자 제거, 없는 문자면 -1 return
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            if j + 1 not in arr:
                arr[j + 1] = keymap[i][j]
            else:
                # 같은 idx 자리에 문자 추가
                arr[j + 1] += keymap[i][j]
            tmp.add(keymap[i][j])   # 없는 문자 찾기

    for i in range(len(targets)):
        res = 0
        for j in range(len(targets[i])):
            # 아예 없는 문자면 -1
            if targets[i][j] not in tmp:
                res = -1
                break
            else:
                res += find(targets[i][j])

        answer.append(res)

    return answer