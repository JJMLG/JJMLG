N = int(input())
company = dict()
result = []
for n in range(N):
    name, el = input().split() # name, enter or leave
    if el == 'enter':
        company[name] = 1
    else: # el == 'leave
        company[name] = 0
for c in company:
    if company[c]:
        result.append(c)
result.sort(reverse=True)
for r in result: print(r)