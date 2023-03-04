N, M = map(int, input().split())
arr = [input() for _ in range(N)]
K = int(input())

ans = 0
chk = set()                             # 확인한 문자열은 또 확인할 필요X
for i in range(N):
    if arr[i] in chk:
        continue
    chk.add(arr[i])

    # i행의 불 전부 켜기 가능?
    cnt = M - sum([int(arr[i][j]) for j in range(M)])   # 0 갯수
    if cnt > K or cnt % 2 != K % 2:     # K보다 작으면 안된다
        continue                        # 홀짝이 안맞으면 안된다

    # 동시에 몇개의 행이 가능? -> 같은 행만 가능!
    same = 0                            # 같은 문자열의 수
    for j in range(i, N):               # 앞은 확인할 필요X
        if arr[i] == arr[j]:
            same += 1
    if same > ans:
        ans = same

print(ans)
