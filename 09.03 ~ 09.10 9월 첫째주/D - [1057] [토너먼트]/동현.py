import sys
import heapq
sys.stdin=open('input.txt')

n,k,l = map(int,input().split())

ls = list(range(1,n+1))
ls[k-1] = 'k'
ls[l-1] = 'l'


def fight(ls):
    global flag
    temp = []
    for i in range(0,len(ls),2):
        
        if ('k' in ls[i:i+2] and 'l' in ls[i:i+2]):
            print(ans)
            exit()

            
        elif 'k' in ls[i:i+2]:
            temp.append('k')
        elif 'l' in ls[i:i+2]:
            temp.append('l')

        else:
            temp.append(1)
    return temp

ans = 0
flag = 0
while len(ls) > 0:
    ans += 1
    # print(ls)
    if flag == 0:
        ls = fight(ls)
    else:
        print(ans)
    
