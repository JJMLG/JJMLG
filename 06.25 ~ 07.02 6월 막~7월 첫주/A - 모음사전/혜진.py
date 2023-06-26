def recur(w, arr):
    if len(w) == 5:
        return
    for a in 'AEIOU':
        arr.append(w + a)
        recur(arr[-1], arr)

def solution(word):
    arr = []                    # 일단 다 만들고
    aeiou = 'AEIOU'
    recur('', arr)
    return arr.index(word) + 1  # 몇 번째인지 리턴
