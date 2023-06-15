def solution(s, skip, index):
    isSkip = [0] * 26
    for sk in skip:
        isSkip[ord(sk) - 97] = 1    # a: 97, z: 122

    ans = ''
    dic = {}                        # before: after
    for i in range(len(s)):
        try:
            ans += dic[s[i]]

        except:
            n = index
            c = ord(s[i]) - 97
            while n:
                nc = 0 if c + 1 == 26 else c + 1    # z를 넘어가면 다시 a로
                if not isSkip[nc]:
                    n -= 1
                c = nc
            dic[s[i]] = chr(c + 97)
            ans += dic[s[i]]
    
    return ans
