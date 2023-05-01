import copy

def solution(skill, skill_trees):
    answer = len(skill_trees)
    dic = {}
    
    for i in range(len(skill)):
        if skill[i] not in dic:
            dic[skill[i]] = i+1
    for tree in skill_trees:
        copyDic = copy.deepcopy(dic)
        flag = 0 
        for i in tree:
            if i in skill:
                if copyDic[i] == min(copyDic.values()):
                    copyDic[i] = 99999
                    pass
                else:
                    answer -= 1
                    flag = 1
                    break
            if flag ==1:
                break
                
    return answer