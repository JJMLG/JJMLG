def solution(s):

    answer = 0
    tmp = ''
    ls = ''
    for i in range(len(s)):
        if s[i].isdigit() == False:
            tmp += s[i]
        else:
            ls += s[i]
        
        if tmp == 'zero':
            tmp = '0'
            ls += tmp
            tmp = ''
        if tmp == 'one':
            tmp = '1'
            ls += tmp
            tmp = ''
        if tmp == 'two':
            tmp = '2'
            ls += tmp
            tmp = ''
        if tmp == 'three':
            tmp = '3'
            ls += tmp
            tmp = ''
        if tmp == 'four':
            tmp = '4'
            ls += tmp
            tmp = ''
        if tmp == 'five':
            tmp = '5'
            ls += tmp
            tmp = ''
        if tmp == 'six':
            tmp = '6'
            ls += tmp
            tmp = ''
        if tmp == 'seven':
            tmp = '7'
            ls += tmp
            tmp = ''
        if tmp == 'eight':
            tmp = '8'
            ls += tmp
            tmp = ''
        if tmp == 'nine':
            tmp = '9'
            ls += tmp
            tmp = ''
    answer=int(ls)
    return answer