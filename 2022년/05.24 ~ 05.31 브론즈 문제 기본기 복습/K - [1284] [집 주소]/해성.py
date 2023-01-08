while True:
    word = input()
    if word == '0':
        break
    else:
        temp =0
        for i in word:
            if int(i)==1:
                temp += 2
            elif int(i)==0:
                temp +=4
            else:
                temp+= 3
        print(temp + len(word)+1)
