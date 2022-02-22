N, M = map(int, input().split())

DNAs = [input() for _ in range(N)]

dictt = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3,
    0: 'A',
    1: 'C',
    2: 'G',
    3: 'T',
}

HD = 0

for i in range(M):

    table = [0] * 4

    for d in DNAs:
        table[dictt[d[i]]] += 1
        
    for j in range(4):
        if j != table.index(max(table)):
            HD += table[j]

    print(dictt[table.index(max(table))], end='')

print()

print(HD)
