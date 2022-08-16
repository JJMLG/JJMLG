for _ in range(int(input())):
    P = input() # parenthesis string : 괄호
    S = [] # stack
    for p in P:
        if p == '(': S.append(p)
        elif p == ')':
            if S: 
                if S[-1] == '(': S.pop()                
            else: S.append(p)
    print('NO' if S else 'YES')

"""
괄호를 하나씩 스택에 집어넣어서
짝이 맞으면 pop해주고
스택이 딱 맞아 떨어지면 괄호의 짝이 맞는 것
스택이 남아있다면 괄호가 짝이 맞지 않는 것
"""