def solution(sequence, k):
    answers = []
    sum = 0
    l = 0
    r = -1

    while True:
        if sum < k:
            r += 1
            if r >= len(sequence):
                break
            sum += sequence[r]
        else:
            sum -= sequence[l]
            if l >= len(sequence):
                break
            l += 1
        if sum == k:
            answers.append([l, r])

    answers.sort(key=lambda x: (x[1] - x[0], x[0]))
    return answers[0]