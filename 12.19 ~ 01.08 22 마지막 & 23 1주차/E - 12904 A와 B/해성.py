S = list(input())
T = list(input())

while len(S) != len(T):
    if T[-1] == "A":
        T.pop()
    else:
        T.pop()
        T.reverse()

if T==S:
    print(1)
else:
    print(0)

