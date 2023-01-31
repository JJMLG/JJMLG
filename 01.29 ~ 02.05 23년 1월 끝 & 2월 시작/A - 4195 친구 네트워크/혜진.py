import sys
input = sys.stdin.readline          # 이거 하고 안하고 속도차이가 너무 많이 남

def find(a):                        # 부모 찾기
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a]) # 부모 찾으면서 최상위 부모로 업데이트 (find 최적화)
        return parent[a]


def union(a, b):                    # 부모 합치기
    pa = find(a)
    pb = find(b)

    if pa == pb:                    # 부모가 같다 == 같은 묶음에 속했다
        return cnt[pa]              # 그 묶음에 속한 사람의 수 == 친구의 수

    if cnt[pa] > cnt[pb]:           # 항상 rank가 낮은 트리를 높이가 높은 트리 밑에 넣는다 (union 최적화)
        parent[pb] = parent[pa]     # 즉, 높이가 더 높은쪽을 root로 한다
        cnt[pa] += cnt[pb]          # cnt가 작은 쪽이 트리구조에서 node가 더 높이 있다고 본다?
        return cnt[pa]

    parent[pa] = parent[pb]         # 반대의 경우 반대로
    cnt[pb] += cnt[pa]
    return cnt[pb]


for _ in range(int(input())):
    N = int(input())
    parent = {}                     # k: 사람, v: 부모 -> 같은 부모를 둔 사람들은 모두 친구(-> 같은 집합)
    cnt = {}                        # k: 사람, v: 그 사람이 속한 친구 집합의 크기

    for _ in range(N):
        fs = input().split()

        for f in fs:
            if f not in parent:
                parent[f] = f
                cnt[f] = 1

        print(union(*fs))
