
def solution(clothes):
    answer = 1
    dict = {k:[] for _,k in clothes}
    for name,category in clothes:
        dict[category].append(name)
    print(dict)
    
    for name in dict.values():
        answer *= (len(name) + 1)
    return answer - 1
    
    return answer
