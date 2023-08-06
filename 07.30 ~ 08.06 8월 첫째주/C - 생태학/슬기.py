import sys
sys.stdin = open('input.txt')

spices = {}

while True:
    try:
        tree = input()
        if tree not in spices:
            spices[tree] = 1
        else:
            spices[tree] += 1
    except:
        break

tmp = sorted(list(set(spices)))


hap = 0
for v in spices.values():
    hap += v

ans = []
for k, v in spices.items():
    for i in tmp:
        if k == i:
            ans.append('{} {:0.4f}'.format(k, v/hap * 100))
ans.sort()
for i in ans:
    print(i)
