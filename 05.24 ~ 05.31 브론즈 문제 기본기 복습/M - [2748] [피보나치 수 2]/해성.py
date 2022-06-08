n = int(input())
record = [0 for _ in range(n+1)]
if n ==1:
    print(1)
else:
    record[1]=1
    record[2]=1
    # print(record)
    for i in range(2, n+1):
        record[i] = record[i-1]+record[i-2]
    print(record[n])
