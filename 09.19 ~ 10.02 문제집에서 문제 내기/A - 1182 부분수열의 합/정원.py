import sys

input = sys.stdin.readline

N, S = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
result = 0
for i in range(1<<N): # N개의 원소를 포함한다, 안한다의 경우가 있으므로 총 경우의 수는 1<<N == 2**N
    seq = [] # 부분수열 초기화
    for j in range(N): # N개 원소들에 대하여 부분수열인지 확인
        if i&(1<<j): seq.append(arr[j]) # &연산을 거친 값이 True라면, j번째 원소는 부분수열에 존재한다
    if sum(seq) == S and len(seq) != 0: result += 1 # 공집합이 아니면서, 부분수열의 합이 S이면 카운트
print(result)