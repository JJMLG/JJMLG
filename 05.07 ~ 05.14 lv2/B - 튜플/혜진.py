def solution(s):
    s = s[2:-2].split('},{')
    s.sort(key=len)
    # print(s)
    ans = []
    for w in s:
        tmp = w.split(',')
        for t in tmp:
            if int(t) not in ans:
                ans.append(int(t))
                break
    return ans