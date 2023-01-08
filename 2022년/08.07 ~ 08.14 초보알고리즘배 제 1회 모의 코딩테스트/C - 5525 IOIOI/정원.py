import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()
result = 0
lst = []
for i in range(len(S)):
    if S[i] == 'I': lst.append(i)
cnt = 0
for i in range(len(lst)-1):
    if lst[i+1] - lst[i] == 2: cnt += 1
    else: cnt = 0
    if cnt >= N: result += 1
print(result)

"""
시간 : 1시간 초과, 정답 풀이 확인
풀이
    제한 시간 1초, 3<=M<=1,000,000 이므로
    O(n) 이하로 코드 동작을 마쳐야 한다
    전체 문자열을 한 번만 탐색한다
    I의 인덱스만 모은 리스트를 생성하여
    리스트에서 두개씩 원소를 비교할 때
    앞 원소와 뒷 원소의 차가 2이면 'IOI'이다
    해당 패턴이 N번 이상일 경우 문제에서 원하는 정답이며
    패턴의 연속됨이 끊어질 시, 카운트를 0으로 돌린다
"""