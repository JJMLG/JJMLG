def solution(a, b, c, d):
    S = set([a, b, c, d])
    C = Counter([a, b, c, d])
    if len(S) == 1:
        return 1111 * a
    if len(S) == 4:
        return min(a, b, c, d)
    if len(S) == 3:
        if a == b: return c * d
        if a == c: return b * d
        if a == d: return b * c
        if b == c: return a * d
        if b == d: return a * c
        if c == d: return a * b
    if C[a] == 2:
        lst = list(S)
        x, y = lst[0], lst[1]
        return (x + y) * abs(x - y)
    if C[a] == 1: x, y = b, a
    if C[b] == 1: x, y = a, b
    if C[c] == 1: x, y = a, c
    if C[d] == 1: x, y = a, d
    return (10 * x + y) ** 2
