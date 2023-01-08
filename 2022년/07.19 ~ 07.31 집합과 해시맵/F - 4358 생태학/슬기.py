import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

species = {}
cnt = 0

while True:
    tree = input().rstrip()
    if not tree:
        break
    if tree in species:
        species[tree] += 1
        # print(species, '----1')
    else:
        species[tree] = 1
        # print(species, '2')
    cnt += 1
    # print(tree)

tree_name = list(species.keys())
tree_name.sort()

for i in tree_name:
    print('%s %.4f' %(i, species[i]/cnt*100))