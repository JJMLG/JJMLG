N = int(input())
C = dict() # company
result = []
for n in range(N):
    name, el = input().split() # name, enter or leave
    if el == 'enter':
        C[name] = 1
    else: # el == 'leave
        C[name] = 0
for c in C:
    if C[c]:
        result.append(c)
result.sort(reverse=True)
for r in result: print(r)