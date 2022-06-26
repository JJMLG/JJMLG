def solution(s):
    # answer = 0
    temp = ''
    change = ''
    eng_number = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                  'nine': 9}
    # print(eng_number)
    for i in s:
        if i.isdigit():
            temp += str(i)
        else:
            change += i
        # print(change)
        if change in eng_number:
            temp += str(eng_number[change])
            change = ''
    # print(temp)

    # print(change)
    return int(temp)