import sys

dict = {}
cnt = 0
while True:
    try:
        a = input()
    except:
        break

    if a in dict:
        dict[a] +=1 
    else:
        dict[a] = 1
    cnt += 1

# for i in dict:
#     dict[i] = round(dict[i] /cnt * 100,4)
for k,v in sorted(dict.items()):
    print("%s %.4f" % (k,v/cnt*100))