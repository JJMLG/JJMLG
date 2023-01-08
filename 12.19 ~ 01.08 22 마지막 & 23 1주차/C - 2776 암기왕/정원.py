for _ in range(int(input())):
    input()
    notes = set(map(int, input().split()))
    input()
    for note in list(map(int, input().split())):
        print(1 if note in notes else 0)