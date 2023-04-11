from copy import deepcopy


def solution(score):
    answer = []

    scores = []

    for i in score:
        scores.append(sum(i) / len(i))

    sort_scores = sorted(scores, reverse=True)

    for i in scores:
        answer.append(sort_scores.index(i) + 1)

    return answer