def solution(clothes):
    dic = {}
    for a, b in clothes:
        try: dic[b] += 1
        except: dic[b] = 1
    # for a, b in clothes:
    #     dic[b] = dic.get(b, 0) + 1
    
    ans = 1
    for v in dic.values():
        ans *= v + 1
    return ans - 1
