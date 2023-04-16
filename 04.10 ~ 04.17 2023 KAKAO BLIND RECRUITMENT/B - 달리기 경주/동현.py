def solution(players, callings):
    answer = []
     
    dic = {}
    for i in range(len(players)):
        dic[players[i]] = i
        
    reverseDic = {v:k for k,v in dic.items()}
    for call in callings:
        dic[call],dic[reverseDic[dic[call]-1]] = dic[call]-1,dic[call]
        reverseDic[dic[call]],reverseDic[dic[call]-1] = reverseDic[dic[call]-1],call
    return list(reverseDic.values())