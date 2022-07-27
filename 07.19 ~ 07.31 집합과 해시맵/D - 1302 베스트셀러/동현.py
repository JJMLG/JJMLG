import sys

dict = {}
n = int(input())
for i in range(n):
    a = input()
    if a not in dict:
        dict[a] = 1
    else:
        dict[a] += 1




maxx = max(dict.values())

result = []
# print(maxx)
for k, v in dict.items():
    # print(k,v)
    if v == maxx:
        result.append(k)

print(sorted(result)[0])
