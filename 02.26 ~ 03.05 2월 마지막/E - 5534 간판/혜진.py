def recur(L, idxs, term):
    if t in ans:                # 이미 사용가능한 간판이면 뒤에 안봐도 됨
        return

    if L == len(name):          # 이름 마지막까지 가능한걸 확인함
        ans.add(t)              # 사용 가능 간판으로 추가
        return
    
    for n in dic[name[L]]:
        if idxs[-1] >= n:       # 알파벳 순서가 거꾸로면 안됨
            continue

        tmp = idxs.copy()       # 숫자만 있는 배열이라 얕은 복사로도 가능
        tmp.append(n)

        if term:                # 간격이 있으면 확인하고 넘겨준다
            if n - idxs[-1] == term:
                recur(L + 1, tmp, term)
        else:                   # 아직 간격 없으면 그냥 넘겨준다
            recur(L + 1, tmp, tmp[1] - tmp[0])


N = int(input())
name = input()

ans = set()
for t in range(N):
    board = input()
    if name == board:
        ans.add(t)
        continue

    dic = { k: [] for k in name }
    for i in range(len(board)):
        if board[i] in dic:
            dic[board[i]].append(i)
    for n in dic[name[0]]:
        recur(1, [n], 0)

print(len(ans))
