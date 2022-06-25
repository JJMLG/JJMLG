import sys
sys.stdin = open('input.txt')

from fractions import Fraction

N = int(input())
stages = list(map(int, input().split()))
# print(stages)

def solution(N, stages):
    fail = []
    # 총 인원
    people = len(stages)
    # print(people)
    answer = []
    # 내림차순(숫자 작으면 먼저)
    # print(Fraction(1,3) + Fraction(1,3))

    now_people = people
    cnt = 0
    for i in range(1, N + 1):
        # 통과 못한 사람 몇 명인지 카운트
        # cnt = 0
        now_people = now_people - cnt
        cnt = 0
        for j in range(people):
            if i == stages[j]:
                cnt += 1

        # 0으로 나눴을 때 처리
        if cnt == 0 and now_people == 0:
            fail.append((0, i))
        else:
            fail.append((Fraction(cnt, now_people), i))
    temp = sorted(fail, key=lambda x: (x[0], -x[1]), reverse=True)
    # print(temp)
    # print(temp[0][1])
    for l in range(len(temp)):
        answer.append(temp[l][1])

    return answer

print(solution(N, stages))