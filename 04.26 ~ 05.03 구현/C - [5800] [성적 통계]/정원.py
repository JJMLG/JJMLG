K = int(input())
for k in range(1, K+1):
    score = list(map(int, input().split()))
    score = score[1:] # 점수의 개수를 나타내는 숫자보다
    # 작은 점수가 있을 수 있음
    # print(score) # 디버깅
    score.sort() # 점수들 정렬
    A, B, C = score[-1], score[0], 0 # 최대 최소 먼저 구하고
    for i in range(len(score)-1):
        if score[i+1]-score[i] > C:
            C = score[i+1]-score[i] # 구간차이가 큰 값을 구해서
    print(f'Class {k}') # 반 번호 출력
    print(f'Max {A}, Min {B}, Largest gap {C}') # 순서대로 출력