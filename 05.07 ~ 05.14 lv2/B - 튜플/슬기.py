def solution(S):
    S = S[2:-2].split("},{")
    numArr = []
    for i in range(len(S)):
        s = S[i].split(",")
        numArr.append(set(s))

    numArr.sort(key=lambda x: len(x))

    ans = set()
    res = []
    for a in numArr:
        tmp = a - ans
        res.append(list(tmp)[0])
        ans = ans | tmp

    res = [int(i) for i in res]
    return res