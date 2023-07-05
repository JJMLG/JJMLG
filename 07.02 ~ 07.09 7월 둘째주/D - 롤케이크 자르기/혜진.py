from collections import Counter

def solution(topping):
    chul = Counter(topping)
    # print(chul)
    bro = {}
    ans = 0
    for top in topping:
        chul[top] -= 1                  # 동생한테 하나 넘겨줌
        bro[top] = bro.get(top, 0) + 1
        if chul[top] == 0:              # 그 토핑이 0개되면 토핑 없앰
            del chul[top]
        if len(chul) == len(bro):       # 같으면 +1
            ans += 1
        elif ans:       # 다른데 이전에 같은적이 있으면
            break       # 이제 동생이 더 많으니까 앞으로 그만 봐도 됨
    return ans
