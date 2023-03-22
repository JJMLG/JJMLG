import sys
input = sys.stdin.readline

n, b, a = map(int, input().split())
price = list(map(int, input().split()))
price.sort()
discount = [False] * n

total = count = 0
for i in range(n):
    if total + price[i] <= b:
        total += price[i]
        count += 1

    else:
        can = False
        for j in range(i, -1, -1):
            if a == 0: break
            if discount[j]: continue
            discount[j] = True
            total -= price[j] // 2
            a -= 1
            if total + price[i] <= b:
                can = True
                total += price[i]
                count += 1
                break
        if not can:
            break

print(count)
