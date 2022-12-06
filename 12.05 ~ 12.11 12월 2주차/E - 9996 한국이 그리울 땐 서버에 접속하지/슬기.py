import sys
sys.stdin = open('input.txt')

n = int(input())
pattern = input().split('*')

for _ in range(n):
    file = input()
    # print(file)
    if len(file) >= 2:
        front = len(pattern[0])
        back = len(pattern[1])
        # print(file[:front])
        # print(file[front:back:])
        if file[:front] == pattern[0]:
            file = file[front:]
            # print(file)
            if file[-back:] == pattern[1]:
                print('DA')
            else:
                print('NE')
        else:
            print('NE')
    else:
        print('NE')