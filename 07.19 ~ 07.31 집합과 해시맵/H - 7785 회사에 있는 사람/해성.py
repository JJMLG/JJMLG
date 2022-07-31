import sys
sys.stdin=open('input.txt')
n= int(input())
record =dict()
name= 0
sta=0
result = []
for i in range(n):
    name, sta = input().split()
    record[name]=sta

record = sorted(record.items(), reverse=True)
# print(record)
for i in record:
    if i[1] == 'enter':
        print(i[0])


