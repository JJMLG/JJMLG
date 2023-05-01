def solution(n, words):
    answer = []
    word = {}
    cnt = 0

    for idx, v in enumerate(words):
        if v not in word:
            word[v] = 0
        else:
            word[v] = idx % n + 1
            cnt = (idx + 1) // n

    for i in range(len(words) - 1):
        if words[i][-1] == words[i + 1][0]:
            continue
        else:
            word[words[i]] = (i + 1) % n + 1
            cnt = (i + 1) // n + 1

    for k, v in word.items():
        if v != 0:
            answer.append(v)
            answer.append(cnt)

    if not answer:
        answer.append(0)
        answer.append(0)

    return answer