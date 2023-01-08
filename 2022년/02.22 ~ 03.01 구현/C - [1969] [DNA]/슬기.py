import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
# dna = [list(input()) for _ in range(n)]
# print(dna)

dna = [input() for _ in range(n)]


# ls = ['T', 'A', 'G', 'C']
# temp = [0, 0, 0, 0]

many = []       # 가장 많이 나온 글자 담을 변수
gap = []        # 다른 글자 나온 숫자 담을 변수
tmp = {'A': 0, 'C': 0, 'G': 0, 'T': 0}      # 글자 나온거 판별할 딕셔너리

for i in range(m):
    if i != 0:              # 0번째는 넣을 필요가 없으니까 그 이후로
        max_key = max(sorted(tmp), key=tmp.get)     # dict에서 가장 많이 나온 글자 & 알파벳순 정렬
        many.append(max_key)
        gap.append(sum(sorted(tmp.values(), reverse=True)[1:]))     # 다르게 나온 글자수 담기

    tmp = {'T': 0, 'A': 0, 'G': 0, 'C': 0}      # 한줄씩 보고 초기화
    # if max(temp)

    for j in range(n):
        # print(dna[j][i])
        if dna[j][i] == 'T':
            # temp[0] += 1
            tmp['T'] += 1
        elif dna[j][i] == 'A':
            # temp[1] += 1
            tmp['A'] += 1
        elif dna[j][i] == 'G':
            # temp[2] += 1
            tmp['G'] += 1
        else:
            # temp[3] += 1
            tmp['C'] += 1

    if i == m-1:                                    # 마지막 글자 검사했을 때 안 들어가서 조건 걸어줌
        max_key = max(sorted(tmp), key=tmp.get)
        many.append(max_key)
        gap.append(sum(sorted(tmp.values(), reverse=True)[1:]))

print(*many, sep='')
print(sum(gap))
"""
세로 줄 비교했을 때 가장 많이 나온 문자열과 다른 문자열이 있으면 카운트
그리고 가장 많이 나온 문자를 출력
"""