from itertools import permutations

N = int(input())
tmp = list(map(int, input().split()))
perm = list(permutations(tmp, N)) # 배열에서 나올 수 있는 모든 경우
maxx = 0 # "차이를 최대로"
for p in perm:
    a = 0 # 해당 배열의 최대값 초기화
    for i in range(N-1):
        a += abs(p[i]-p[i+1]) # 앞뒤 값의 절대값 더하기
    if a > maxx: # 최대값 갱신이 가능하면
        maxx = a # 최대값 갱신
print(maxx) # 출력