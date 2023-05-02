def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees:
        tmp = ''
        for j in i:
            if j in skill:
                tmp += j

        if skill[:len(tmp)] == tmp:
            answer += 1
            # print(skill[:len(tmp)])

    return answer