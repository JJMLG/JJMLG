from collections import defaultdict

"""
0: ZERO     Z
1: ONE      마지막 O
2: TWO      W
3: THREE    2, 8 다음 T
4: FOUR     0, 3 다음 R
5: FIVE     4 다음 F
6: SIX      X
7: SEVEN    6 다음 S
8: EIGHT    G
9: NINE     5, 6, 8 다음 I

0, 2, 6, 8, 3, 4, 5, 7, 9, 1
"""

def delete(strnum: str, cnt: int):
    for c in strnum:
        dic[c] -= cnt

for t in range(int(input())):
    s = input()
    order = {
        'Z': (0, 'ZERO'), 'W': (2, 'TWO'), 'X': (6, 'SIX'), 'G': (8, 'EIGHT'), 'T': (3, 'THREE'),
        'R': (4, 'FOUR'), 'F': (5, 'FIVE'), 'S': (7, 'SEVEN'), 'I': (9, 'NINE'), 'O': (1, 'ONE')
    }

    # 각 알파벳이 몇번씩 나왔는지
    dic = defaultdict(int)
    for c in s:
        dic[c] += 1

    ans = ''
    # order 순서대로 돌면서 input값에 존재하지 않으면 continue
    for k in order:
        if not dic[k]: continue
        # 존재하면 그 갯수만큼 더해준다
        ans += str(order[k][0]) * dic[k]
        # 그 숫자에 해당하는 알파벳은 나온 수 만큼 빼준다
        delete(order[k][1], dic[k])

    ans = sorted(list(ans))
    ans = ''.join(ans)

    print(f'Case #{t + 1}: {ans}')
