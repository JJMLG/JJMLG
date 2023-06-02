from itertools import permutations


def solution(babbling):
    answer = 0

    speak = ["aya", "ye", "woo", "ma"]

    for j in babbling:
        for i in speak:
            if i * 2 not in j:
                j = j.replace(i, ' ')
                # print(j)
        if j.strip() == '':
            answer += 1


    # 테케 1, 4, 7 --- 틀림
    # speak = ["aya", "ye", "woo", "ma"]
    #
    # tmp = []
    # for i in range(1, len(speak) + 1):
    #     for j in permutations(speak, i):
    #         string = ''
    #         for k in j:
    #             string += k
    #         tmp.append(string)
    #
    # # print(tmp)
    #
    # for i in babbling:
    #     for j in tmp:
    #         if i == j:
    #             print(i)
    #             answer += 1

    return answer