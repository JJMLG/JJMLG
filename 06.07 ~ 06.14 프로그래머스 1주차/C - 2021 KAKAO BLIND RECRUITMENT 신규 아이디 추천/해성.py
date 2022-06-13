def solution(new_id):
    result = ''
#     소문자 치환
    new_id = new_id.lower()
    for i in new_id:
        if i.islower() == True or i.isdigit()==True or i =='-' or i == '_' or i =='.':
# 숫자면 문자열로
            if i.isdigit()==True:
                result += str(i)
            else:
                result +=i
    # print(result, "결과")
    temp = result[0]+''
#     3단계
    for i in range(1, len(result)):
        if result[i]=="." and result[i-1] ==".":
            pass
        else:
            temp+=result[i]
#     4단계
    print(temp)
    if len(temp)>0 and temp[0] == '.':
        temp = temp.lstrip('.')
    if len(temp)>0 and temp[-1] == '.':
        temp = temp.rstrip('.')
#     5단계
    if len(temp)==0:
        temp = 'a'
#     6단계
    if len(temp)>=16:
        temp = temp[:15]
        if temp[-1]=='.':
            temp = temp[:14]
#    7단계
    if len(temp)<=2:
        while len(temp)< 3:
            temp += temp[-1]
    answer= temp
    # answer = new_id
    return answer