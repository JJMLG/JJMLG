import sys

input = sys.stdin.readline

N, M = map(int, input().split())
time = sorted(list(int(input()) for _ in range(N)))
start = 0
# time의 최소값 * 사람 수 => 최대 시간 
end = min(time) * M # Worst Case : 모든 입국 심사자가 1번 심사대를 통과하려고 떼쓰는 경우
result = 0
while start <= end :
    mid = (start + end) // 2
    I = 0 # immigration : 입국심사
    for t in time: I += mid // t # mid초 동안 심사대를 통과할 수 있는 사람 수
    if I >= M: # mid초 동안 M명 이상 심사대를 통과할 수 있음
        end = mid-1 # 더 작은 시간 탐색
        result = mid # 매개 변수 탐색 : 최소값 저장
    else: start = mid+1 # mid초 동안 M명 이상 심사대를 통과할 수 없음
print(result)

"""
시간을 기준으로 이분탐색한다
예제1같이 28초의 경우, 1번 심사대가 4명을 심사한다
"이번 mid초 동안 몇명이 심사대를 통과할 수 있는가"를 확인하여
start<=end 인 동안 M명을 심사할 수 있는 시간초를
이분탐색으로 줄여나간다
"""