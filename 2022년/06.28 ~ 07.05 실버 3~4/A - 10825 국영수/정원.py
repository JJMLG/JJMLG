arr = [] # 성적표 배열
for n in range(int(input())):
    tmp = input().split() # 성적을 입력받아서
    for i in range(4): # 성적을 int형으로 변환
        try: tmp[i] = int(tmp[i])
        except: pass
    arr.append(tmp) # 성적표에 추가
"""
lambda에서 정렬 자체를 역순서로 할 수는 없지만
숫자의 경우 값을 음수(-)로 만들어주어 역정렬을 할 수 있음
"""
arr.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))
# 국어는 내림차순, 영어는 오름차순, 수학은 내림차순, 이름은 오름차순
for a in arr: print(a[0]) # 출력