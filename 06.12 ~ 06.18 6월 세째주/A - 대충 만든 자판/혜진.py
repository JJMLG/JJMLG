def solution(keymap, targets):
    dic = {}                            # 키: 눌러야 하는 최소 횟수
    for key in keymap:
        for i in range(len(key)):
            try:                        # 최소로 업데이트
                dic[key[i]] = min(dic[key[i]], i + 1)
            except:                     # 없으니까 초기화
                dic[key[i]] = i + 1

    ans = [0] * len(targets)
    for i in range(len(targets)):
        cnt = 0                         # 몇 번 눌러야 하는지
        for t in targets[i]:
            try:
                cnt += dic[t]
            except:                     # 키가 없으면 그 문자열은 -1
                cnt = -1
                break
        ans[i] = cnt
    
    return ans
