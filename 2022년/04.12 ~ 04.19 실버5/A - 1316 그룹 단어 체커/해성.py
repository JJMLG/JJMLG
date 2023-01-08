import sys
sys.stdin = open('1316.txt')

N = int(input())
count = 0
for _ in range(N):
    words = input()
    result = set()
    temp = ''
    if len(words) == 1:
        count += 1
    else:
        count += 1
        for i in range(1, len(words)):
            result.add(words[i-1])
            if words[i]!=words[i-1]:

                if words[i] in result:
                    count -= 1
                    break
print(count)