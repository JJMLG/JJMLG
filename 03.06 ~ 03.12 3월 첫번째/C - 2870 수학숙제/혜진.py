N = int(input())
nums = []

for _ in range(N):
    string = input()
    tmp = ''
    for s in string:
        if s.isdigit():
            tmp += s
        elif tmp:   # 알파벳인데 tmp가 있으면 리스트에 추가 / 알파벳인데 tmp가 없으면 걍 pass
            nums.append(int(tmp))
            tmp = ''
    if tmp:         # 마지막이 숫자로 끝난 경우
        nums.append(int(tmp))

for n in sorted(nums):
    print(n)
