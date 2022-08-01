N = int(input())
N_list = list(map(int, input().split()))
dct = {}
for n in N_list:
    try: dct[n] += 1
    except: dct[n] = 1
M = int(input())
M_list = list(map(int, input().split()))
for m in M_list:
    try: print(dct[m], end=' ')
    except: print(0, end=' ')