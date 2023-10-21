import sys
sys.stdin = open('input.txt')

t = int(input())

for _ in range(t):
    n = int(input())
    # graph = [[] * (n+5)]
    # visited = [[] * (n+5)]
    par = [0] * (n+5)   #각 노드의 부모노드 저장
    for _ in range(n-1):
        a, b = map(int, input().split())
        par[b] = a      #부모 노드 저장
    ta, tb = map(int, input().split())

    a_par = [ta]
    b_par = [tb]

    # 각노드의 부모노드가 루트일때까지 모두 저장
    while par[ta]:
        a_par.append(par[ta])
        ta = par[ta]

    while par[tb]:
        b_par.append(par[tb])
        tb = par[tb]

    # 같은 레벨로 맞추고 부모노드 같은거 찾기
    a_lev = len(a_par) - 1
    b_lev = len(b_par) - 1

    # 루트노드부터 차례대로 비교
    while a_par[a_lev] == b_par[b_lev]:     #부모노드가 같지 않을때까지
        a_lev -= 1
        b_lev -= 1

    print(a_par[a_lev+1])



