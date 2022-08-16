N = int(input())
lst = list(map(int, input().split()))
A, result, cnt = 0, 0, 0 # archor
for l in lst:
    # 봉우리 높이 갱신, 임시값 초기화, 결과값 갱신
    if l > A: A, cnt, result = l, 0, max(result, cnt)
    else: cnt += 1
print(max(result, cnt)) # 봉우리를 갱신하지 않고 for문이 끝난 경우가 있을 수 있음

"""
그리디 문제
출발한 높이보다 더 높은 봉우리에 부딪히기 전까지
몇개의 봉우리를 만나는지
가장 많이 만난 봉우리의 수는 몇인지를 구하는 문제

최소최대값 갱신을 여태
if a > b: a = b
를 사용했었는데
a = max(a, b)
로 바꾸는 것도 좋을 것 같다
"""