def solution(msg):
    ans = []
    dic = { chr(i + 64): i for i in range(1, 27) }  # {'A': 1, 'B': 2, ..., 'Z': 26 }

    i = 0                                           # 시작 글자 index
    while i < len(msg):
        w = msg[i]                                  # 현재 입력(w)
        j = i + 1                                   # 다음 글자 index
        while j < len(msg):
            try:
                dic[w + msg[j]]                     # 다음 글자 붙인게 가능하면
                w += msg[j]                         # 현재 입력 업데이트
                j += 1                              # 다음 글자 업데이트
            except:
                break                               # 불가능하면 그만
        ans.append(dic[w])                          # 현재 입력 출력

        if j == len(msg):                           # 다음 글자 index가 벗어났으면 그만
            break
        else:                                       # 벗어나지 않았으면 사전에 추가
            dic[w + msg[j]] = len(dic) + 1
            i = j                                   # 시작 글자 index 업데이트

    return ans