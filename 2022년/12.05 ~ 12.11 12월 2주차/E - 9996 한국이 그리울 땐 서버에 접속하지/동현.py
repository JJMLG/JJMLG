import sys
sys.stdin = open('input.txt')

n = int(input())
name = input()
first = name.split('*')[0]
second = name.split('*')[1]

for _ in range(n):
    file = input()
    
    # for i in range(len(first)):
  
    #     if first[i] != file[i]:
    #         print('NE')
    # print(file[:len(first)])
    # print(file[len(file)-len(second):])
    # print(len(file[:len(first)]) + len(file[len(file)-len(second):]))
    if file[:len(first)] != first:
        print('NE')
        continue
    if file[len(file)-len(second):] != second:
        print('NE')
        continue
    if len(name) -1 > len(file):
        print('NE')
        continue
    print('DA')
    # for j in range(len(file)-len(second),len(file)):
    #     print(len(file),len(second))
        # if second[j] != file[j]:
        #     print('NE')
    # print('DA')
        
    # print(first,second)
