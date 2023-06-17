def solution(s, skip, index):
    answer = ''

    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    alpha = set(alpha)  # 어차피 중복 없음 차집합 하려고 set
    skip = set(skip)    # 어차피 중복 없음 차집합 하려고 set
    delete_skip = alpha - skip  # skip 빼주기
    delete_skip = list(delete_skip)
    delete_skip.sort()  # 정렬하기

    for j in s:
        for i in delete_skip:
            if i == j:
                aa = (delete_skip.index(i) + index) % len(delete_skip)
                tmp = delete_skip[aa]
                answer += tmp

    return answer