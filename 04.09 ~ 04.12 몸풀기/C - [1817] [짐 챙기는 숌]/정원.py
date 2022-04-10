N, M = map(int, input().split())
if N > 0: # 담아야 할 책이 있으면
    books = list(map(int, input().split()))
    result = 1 # 상자를 하나 가져다 놓고
    box = M # 상자에 담을 수 있는 무게는 M
    for book in books: # 책들을 순회하면서
        box -= book # 상자에 책을 하나씩 담는다
        if box < 0: # 상자에 책을 담을 수 없으면
            box = M - book # 다음 상자를 가져와 책을 담고
            result += 1 # 상자 개수를 +1
else: # 담아야 할 책이 없으면
    result = 0 # 필요한 상자의 개수는 0
print(result)