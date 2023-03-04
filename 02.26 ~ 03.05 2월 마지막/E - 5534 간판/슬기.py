import sys
sys.stdin = open('input.txt')

n = int(input())
name = input()
old = [input() for _ in range(n)]
print(old)
s_old = old
visited = [0] * (len(old)+1)
cnt = 0

tmp = []
for i in old:
    if name in i:
        cnt += 1
    else:
        s = i.index(name[0])
        e = i.index(name[-1])
        for k in range(len(i)):
            if i[k] == name[0]:
                if s >= k:
                    s = k
            elif i[k] == name[-1]:
                if e >= k:
                    e = k
            print(s, e)

        new_i = i[s:e+1]
        print(new_i)

# tmp.sort()
print(tmp)
print(cnt)