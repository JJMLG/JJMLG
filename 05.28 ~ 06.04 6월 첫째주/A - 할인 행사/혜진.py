from collections import Counter

def solution(want, number, discount):
    dic = {}                                        # 원하는 제품: 수
    for i in range(len(want)):
        dic[want[i]] = number[i]

    ans = 0
    for i in range(len(discount) - 9):
        if dic == Counter(discount[i : i + 10]):    # i부터 i + 9까지 { 제품: 수 } 객체
            ans += 1
    return ans
