N, M = map(int, input().split())
L = set() # listened
for n in range(N): L.add(input())
result = []
for m in range(M):
    s = input()
    if s in L:
        result.append(s)
result.sort()
print(len(result))
for r in result: print(r)

"""
"듣도 못한" 배열을 읽어올 시, list 사용 시 시간초과, set 사용 시 맞았습니다!
문제 조건에 입력값의 중복이 없다고 이미 나와있지만
중복제거 목적이 아닌 시간단축을 위해서 set를 사용
"""