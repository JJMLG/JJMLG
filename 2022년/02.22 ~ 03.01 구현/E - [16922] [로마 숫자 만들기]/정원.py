from itertools import combinations_with_replacement as comb
# itertools를 코테에서도 쓸 수 있다고 하니
# 실력향상을 위한 빡구현 vs 일단 라이브러리 사용
# 고민해볼 가치가 있을 듯 (아래는 참고 블로그 링크)
# https://uni2237.tistory.com/56


N = int(input())
result = [] # 경우의 수 들이 담길 리스트
rome = [1, 5, 10, 50] # 로마숫자 IVXL

for temp in comb(range(4), N):
    summ = 0 # 매 경우의 수
    # N==2 일 때, temp = (0, 0) ...
    for i in temp:
        summ += rome[i] # i는 rome의 인덱스값으로 사용

    result.append(summ) # 경우의 수를 완성해서 
    # result에 추가

print(len(set(result))) # set으로 중복제거