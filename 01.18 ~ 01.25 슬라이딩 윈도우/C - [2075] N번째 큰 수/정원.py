import heapq # 우선순위 큐

N = int(input())

hq = heapq # 힙큐 메서드 사용하기 위함

result = [] # 힙큐로 담을 리스트

# 일단 첫 줄을 힙큐로 넣는다
for i in list(map(int, input().split())):
    hq.heappush(result, i)

# 두번째줄부터
for n in range(1, N):
    # 매 줄 마다 힙큐에 넣는 동시에 pop 해주면서
    # N개로 개수를 맞춘다
    for i in list(map(int, input().split())):
        # 개사기메서드 힙푸시팝
        hq.heappushpop(result, i)

# 입력받는 동시에 힙푸시팝을 진행하고 남은 리스트의
# 첫번째 값이 정답    
print(hq.heappop(result))