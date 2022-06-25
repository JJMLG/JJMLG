def solution(s):
    answer = ''
    numbers = ['zero', 'one','two','three', 'four','five','six','seven','eight','nine']
    temp=''
    for i in s:
        if i.isdigit():
            answer+=i
            if temp:
                answer+=str(numbers.index(temp))
                temp=''
        else:
            temp+=i
            if temp in numbers:
                answer+=str(numbers.index(temp))
                temp = ''
    if temp:
        answer+=str(numbers.index(temp))
    answer = int(answer)
    return answer