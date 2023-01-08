from collections import defaultdict

N = int(input())
pl = {}
lp = defaultdict(list)      # 같은 난이도의 문제가 여러개일 수 있으니 list를 default로

def add(p, l):
    if p in pl:             # 문제번호가 존재하면 새로운 난이도로 들어가야하니까
        lev = pl            # 기존 난이도에 있는 문제 번호를 지워야함
        lp[lev].remove(p)
    pl[p] = l               # 이건 덮어쓰기 가능
    lp[l].append(p)         # 문제번호 추가하기

for _ in range(N):          # 첫 입력
    p, l = map(int, input().split())
    add(p, l)

M = int(input())
for _ in range(M):
    lst = input().split()

    if lst[0] == "add":     # 추가
        add(int(lst[1]), int(lst[2]))

    elif lst[0] == "solved":
        p = int(lst[1])
        l = pl[p]
        del pl[p]
        lp[l].remove(p)
        if not lp[l]:       # 빈 리스트면 이후 출력에 방해되지않게 key값 지우기!!
            del lp[l]

    else:
        # print(lp)         # 33번줄 안해줘서 여기서 빈 리스트가 있는 key를 발견함
        if lst[1] == "1":
            maxL = max(lp.keys())
            print(max(lp[maxL]))
        else:
            minL = min(lp.keys())
            print(min(lp[minL]))
