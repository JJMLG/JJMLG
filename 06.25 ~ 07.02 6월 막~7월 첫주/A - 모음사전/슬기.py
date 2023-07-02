from itertools import product   # 중복 순열

def solution(word):
    answer = []
    li = ['A', 'E', 'I', 'O', 'U']

    for i in range(1, 6):
        for per in product(li, repeat=i):
            answer.append(''.join(per))
    answer.sort()

    return answer.index(word) + 1