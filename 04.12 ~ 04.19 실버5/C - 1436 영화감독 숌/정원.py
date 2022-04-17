N = int(input())
cnt = 0 # 몇번째 666인가
six3 = 666 # 666부터 출발
while True:
    if '666' in str(six3): # 종말숫자면
        cnt += 1 # 카운트 +1
    if cnt == N: # N번째 종말숫자면
        print(six3) # 값을 출력
        break # while문 종료
    six3 += 1 # 다음 숫자는 종말숫자인가