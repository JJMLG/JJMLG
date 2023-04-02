from itertools import permutations


def solution(babbling):
    answer = 0
    talk = ["aya", "ye", "woo", "ma"]

    tmp = []
    for i in range(1, len(talk) + 1):
        for j in permutations(talk, i):
            word = ''
            for k in j:
                word += k
            tmp.append(word)

    # print(tmp)

    for i in babbling:
        if i in tmp:
            # print(i)
            answer += 1

    return answer