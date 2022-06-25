def solution(new_id):
    result = ''
#  1단계 소문자 치환
    new_id = new_id.lower()
#  2단계 소문자거나, 숫자거나, 빼기, 밑줄, 마침표이면
    for i in new_id:
        if i.islower() == True or i.isdigit()==True or i =='-' or i == '_' or i =='.':
# 근데 숫자면 문자열로 변환 아니면 그대로 result에 추가
            if i.isdigit()==True:
                result += str(i)
            else:
                result +=i
    # print(result, "결과")
#     앞뒤봐야하므로 맨처음은 일단 temp에 붙여놓고
#  그뒤것들 중에 .연속인거 빼기
    temp = result[0]
#     3단계 마침표 연속 두개면 빼기
    for i in range(1, len(result)):
        if result[i]=="." and result[i-1] ==".":
            pass
        else:
            temp+=result[i]
#     4단계
    # print(temp)
#    temp가 0보다 길고 처음이 .이거나 맨뒤가.이면 제거
# .두개인경우왜 제거 안해도 되는지 궁금쓰
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