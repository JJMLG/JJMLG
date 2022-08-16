import sys
sys.stdin = open('input.txt')

n = int(input())


temp = ''
cnt = 0
for _ in range(n):
    word = list(input())
    stack = []
    # for i in range(len(word)-1):
    #     if word[i] == word[i+1]:
    #         cnt += 1
    #         stack.append(word[i+1])
    #         stack.append(word[i])
    # print(stack)
    i = 0
    while True:
        if i == len(word)-1:
            break
        if word[i] == word[i+1]:
            cnt += 1
            stack.append(word[i+1])
            stack.append(word[i])
            # i += 1
        i += 1
    print(stack)