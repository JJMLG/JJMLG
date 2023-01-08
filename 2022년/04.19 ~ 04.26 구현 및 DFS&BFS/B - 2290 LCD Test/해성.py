s, n = map(int,input().split())
n=str(n)

result = [[] for _ in range(2*s+3)]
for i in range(len(str(n))):
    if int(n[i])==0:
        for i in range(2 * s + 3):
            if i == 0 or i == 2 * s + 2:
                result[i].append((" " + "-" * s + " "))
            elif i == s + 1:
                result[i].append((" " * (s + 2)))
            else:
                result[i].append(("|" + " " * s + "|"))
    elif int(n[i])==1:
        for i in range(2*s+3):
            # 처음일 때, 마지막일 때, 중간일 때
            if i ==0 or i == 2*s+2 or i ==s+1:
                result[i].append((" "*(s+2)))
                # print(i)
            else:
                # print(i)
                result[i].append((" "*(s+1)+'|'))
    elif int(n[i])==2:
        for i in range(2 * s + 3):
            if i == 0 or i == 2 * s + 2 or i ==s+1:
                result[i].append((" " + "-" * s + " "))
            elif i == s + 1:
                result[i].append((" " * (s + 2)))
                # print(i)
            elif i > 0 and i < s + 1:
                # print(i)
                result[i].append((" " * (s+1) + "|"))
            else:
                # print(i)
                result[i].append(("|" + " " * (s+1)))
    elif int(n[i])==3:
        for i in range(2 * s + 3):
            if i == 0 or i == 2 * s + 2 or i ==s+1:
                result[i].append((" " + "-" * s + " "))
            elif i == s + 1:
                result[i].append((" " * (s + 2)))
                # print(i)
            else:
                result[i].append((" " * (s+1) + "|"))
    elif int(n[i])==4:
        for i in range(2*s+3):
            if i ==0 or i == 2*s+2:
                result[i].append((" "*(s+2)))
                # print(i)
            elif i ==s+1:
                result[i].append((" " + "-" * s + " "))
            elif i > 0 and i < s + 1:                # print(i)
                result[i].append(('|'+" "*s+'|'))
            else:
                result[i].append((" " * (s+1) + "|"))
    elif int(n[i])==5:
        for i in range(2 * s + 3):
            if i == 0 or i == 2 * s + 2 or i ==s+1:
                result[i].append((" " + "-" * s + " "))
            elif i == s + 1:
                result[i].append((" " * (s + 2)))
                # print(i)
            elif i > 0 and i < s + 1:
                # print(i)
                result[i].append(("|" + " " * (s + 1)))
            else:
                # print(i)
                result[i].append((" " * (s + 1) + "|"))
    elif int(n[i])==6:
        for i in range(2 * s + 3):
            if i == 0 or i == 2 * s + 2 or i ==s+1:
                result[i].append((" " + "-" * s + " "))
            elif i == s + 1:
                result[i].append((" " * (s + 2)))
                # print(i)
            elif i > 0 and i < s + 1:
                # print(i)
                result[i].append(("|" + " " * (s + 1)))
            else:
                result[i].append(("|"+ ' ' * s + "|"))
    elif int(n[i])==7:
        for i in range(2*s+3):
            if i == 0:
                result[i].append((" " + "-" * s + " "))
            elif i == 2*s+2 or i ==s+1:
                result[i].append((" "*(s+2)))
                # print(i)
            else:
                # print(i)
                result[i].append((" "*(s+1)+'|'))
    elif int(n[i])==8:
        for i in range(2 * s + 3):
            if i == 0 or i == 2 * s + 2 or i ==s+1:
                result[i].append((" " + "-" * s + " "))
            elif i == s + 1:
                result[i].append((" " * (s + 2)))
                # print(i)
            else:
                # print(i)
                result[i].append(("|" + " " * s + "|"))
    elif int(n[i])==9:
        for i in range(2 * s + 3):
            if i == 0 or i == 2 * s + 2 or i ==s+1:
                result[i].append((" " + "-" * s + " "))
            elif i == s + 1:
                result[i].append((" " * (s + 2)))
                # print(i)
            elif i > 0 and i < s + 1:
                # print(i)
                result[i].append(("|" + " " * s+"|"))
            else:
                # print(i)
                result[i].append((" " * (s + 1) + "|"))
for i in result:
    print(*i)