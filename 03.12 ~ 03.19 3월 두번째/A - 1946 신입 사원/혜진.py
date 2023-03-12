T = int(input())
for _ in range(T):
    N = int(input())
    ranks = [list(map(int, input().split())) for _ in range(N)]
    ranks.sort()

    ans = 1                                 # 맨앞 사람은 서류1등이라서 무조건 합격
    standardRank = ranks[0][1]              # 그 사람의 면접 랭크를 기준으로 추가 합격자 찾기
    for i in range(N):
        if standardRank > ranks[i][1]:      # 면접을 더 잘봤으면
            ans += 1                        # 합격
            standardRank = ranks[i][1]      # 기준은 이 사람으로 바뀜. 그러면 이후에도 이전 standardRank보다는 자동으로 높은 랭킹이니까

    print(ans)
