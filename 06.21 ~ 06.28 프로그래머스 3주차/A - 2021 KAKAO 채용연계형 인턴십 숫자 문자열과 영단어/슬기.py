def solution(s):
    # answer = 0
    temp = ''
    change = ''

    # 영어 > 숫자로 변환
    eng_number = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                  'nine': 9}

    for i in s:
        # 숫자면 그대로
        if i.isdigit():
            temp += str(i)

        # 문자면 변환해줄 수 있을만큼 더해주기 예 o + n + e
        else:
            change += i

        # 완성된 문자열(one)이 변환할 딕셔너리에 있다면
        if change in eng_number:
            # 숫자로 변환(문자열로 변경해서 더해줌)
            temp += str(eng_number[change])
            # 초기화
            change = ''
            # 숫자로 출력
    return int(temp)