import sys
sys.stdin=open('input.txt')
# N = int(input())
# books = dict()
# n=''
# maxbooks=''
# for i in range(N):
#     n = input()
#     if n in books:
#         books[n]+=1
#     else:
#         books[n] = 1
# maxx=0
# maxbooks=chr(ord('z')+1)
# books = sorted(books.items())
# for i in books:
#     print(i[1])
#     if maxx < i[1]:
#         maxx=i[1]
#         maxbooks=i[0]
# print(maxbooks)
# ------------------------------------------------------------------------

N = int(input())
books = list(input() for _ in range(N))
books.sort()
books.append(chr(ord('z')+1))
maxx=0
sum=0
maxbook=books[len(books)-1]
result=''
def checkLength(a,b):
    lena, lenb = 0, 0
    lena = len(a)
    lenb = len(b)
    temp=''
    words=''
    if lena>lenb:
        temp=lenb
        word=b
    else:
        temp =lena
        word = a
    for i in range(temp):
        if ord(a[i]) < ord(b[i]):
           return a
        elif ord(a[i]) == ord(b[i]):
            continue
        else:
            return b
    return word

for i in range(len(books)-1):
    sum += 1
        # 마지막이면 지금까지 계산
    if(books[i]!=books[i+1]):
        # 앞이랑 지금이랑 다르면
        if(maxx<sum):
            maxx=sum
            maxbook=books[i]
            sum=0
        elif maxx==sum:
            result = checkLength(books[i], maxbook)
            maxbook=result
            sum=0
print(maxbook)

