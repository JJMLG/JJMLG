import sys
sys.stdin = open('input.txt')

t = int(input())

temp = []

for _ in range(t):
    parenthesis = list(input())
    print(parenthesis)

    for i in range(len(parenthesis)-1, -1, -1):
        print(parenthesis.pop(), i)