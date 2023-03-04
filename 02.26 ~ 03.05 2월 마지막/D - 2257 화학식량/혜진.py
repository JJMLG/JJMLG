chemical = input()
weight = {'H': 1, 'C': 12, 'O': 16}     # 각 원자의 질량 dict
stack = []

for c in chemical:
    if c == '(':
        stack.append(c)

    elif c == ')':                      # '('가 나올때까지 숫자를 더한다
        tmp = 0
        while True:
            try: tmp += stack.pop()     # 숫자면 더한다
            except: break               # '('면 break
        stack.append(tmp)               # 더한 값을 추가

    elif c.isdigit():                   # 숫자면 곱하기
        stack[-1] *= int(c)

    else:                               # 알파벳이면 질량을 추가
        stack.append(weight[c])

print(sum(stack))                       # stack에 있는 질량을 모두 더한다
