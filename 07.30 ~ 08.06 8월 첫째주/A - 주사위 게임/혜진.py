from collections import Counter

def solution(a, b, c, d):
    S = set([a, b, c, d])
    C = Counter([a, b, c, d])
    if len(S) == 1:                 # p, p, p, p
        return 1111 * a
    if len(S) == 4:                 # p, q, r, s
        return min(a, b, c, d)
    if len(S) == 3:                 # p, p, q, r
        if a == b: return c * d
        if a == c: return b * d
        if a == d: return b * c
        if b == c: return a * d
        if b == d: return a * c
        if c == d: return a * b
    if C[a] == 2:                   # p, p, q, q
        lst = list(S)
        x, y = lst[0], lst[1]
        return (x + y) * abs(x - y)
    if C[a] == 1: x, y = b, a       # p, p, p, q
    if C[b] == 1: x, y = a, b
    if C[c] == 1: x, y = a, c
    if C[d] == 1: x, y = a, d
    return (10 * x + y) ** 2
