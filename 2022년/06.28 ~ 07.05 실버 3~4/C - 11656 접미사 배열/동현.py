import sys

s = input()
ls = []

for i in range(len(s)):
    ls.append(s[i:])
a = sorted(ls)

for j in range(len(a)):
    print(a[j])