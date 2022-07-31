import sys
sys.stdin=open('input.txt')
# ins = dict()
# outs =dict()
N = int(input())
ins=[0 for _ in range(N)]
outs=[0 for _ in range(N)]
for i in range(N*2):
    car = input()
    if i < N:
        ins[i] = car
    else:
        outs[i-N]=car
sums=0
n = 0
m = 0
find = 0
for i in range(len(ins)):
    try:
        n = outs.index(ins[i])
    except:
        continue
    outs = outs[n+1:]
    sums += n
    if len(outs)<=1:
            print(sums)
            break