s = input()
result = []
for i in range(len(s)):
    result.append(s[i:])
    result.sort()
for j in result:
    print(j)

