import sys

input = sys.stdin.readline

def dfs(start):
    if len(result) == M: # 수열이 완성됐다면
        print(*result) # 완성된 수열 출력
        # 이번 함수가 종료되고 나오면서 line14의 result.pop()에서 마지막 숫자 제거
    else: # 아직 수열이 완성되지 않았다면
        for i in range(start, N): # 수열에 더 들어올 남은 숫자 개수만큼 for
            if nums[i] not in result:
                result.append(nums[i]) # nums[i]를 집어넣고
                dfs(i+1) # 더 깊이 탐색
                result.pop() # 방금 넣었던 nums[i]를 빼주기

N, M = map(int, input().rstrip().split())
nums = sorted(list(map(int, input().rstrip().split())))
result = []
dfs(0)