
import sys
from collections import deque
from pprint import pprint
sys.stdin = open('input.txt')


ls = list(input())


def small():
    stack = []
    result = []
    for i in range(len(ls)):
        
        if stack == []:
            if ls[i] == 'M':
                stack.append('1')
                result.append('M')
            else:
                stack.append('5') 
                result.append('K')
        else:
            if ls[i] == 'M':
                if result[-1] == 'M':
                    stack.append('0')
                    
                else:
                    stack.append('1')
                result.append('M')
            else:
                stack.append('5')
                result.append('K')

    return ''.join(stack)

def big():
    stack = []
    tmp = []
    for i in range(len(ls)):
        if ls[i] == 'M':
            tmp.append('M')
        else:
            if tmp == []:
                stack.append('5')
            else:
                stack.append(str(5*10**len(tmp)))
                tmp = []
    
    if tmp:
        stack.append('1'*len(tmp))
    return ''.join(stack)
        

print(big())
print(small())