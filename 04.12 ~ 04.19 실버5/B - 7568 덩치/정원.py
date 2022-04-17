N = int(input())
wnhs = [] # 덩치 리스트
result = [] # 덩치 순위 리스트
for n in range(N): # N명의
    wnhs.append(tuple(map(int, input().split()))) # 덩치 입력
# N * N 
for i in range(N): # 5명의 덩치를 비교
    cnt = 1 # 덩치를 비교하기 전까지는 모두가 덩치 1등
    for j in range(N):
        # 본인보다 덩치가 큰 사람이 있다면
        if i != j and wnhs[i][0] < wnhs[j][0] and wnhs[i][1] < wnhs[j][1]:
            cnt += 1 # 덩치 순위 +1
    result.append(cnt) # 덩치 순위 추가
print(*result) # 출력
