import sys

input = sys.stdin.readline

N, P = map(int, input().split()) # 놀랍게도 프렛은 영어도 Fret이다
stack, result = [[] for _ in range(7)], 0 # 기타줄은 여섯줄 인덱스 맞추기
print(stack)
for n in range(N):
    S, F = map(int, input().split()) # string, fret
    if not stack[S]:
        stack[S].append(F)
        result += 1
    else: # stack[S]
        if F > stack[S][-1]:
            stack[S].append(F)
            result += 1
        elif F < stack[S][-1]:
            # 같거나 더 낮은 프렛을 만날 때 까지 pop
            while stack[S] and F < stack[S][-1]:
                stack[S].pop()
                result += 1
            # 누른 손을 모두 떼거나, 더 낮은 프렛을 만났을 경우
            if not stack[S] or stack[S][-1] < F:
                stack[S].append(F)
                result += 1
        else: # F == stack[-1]
            pass
    print(stack)
    print(result)
    print()
print(result)

"""
예제 1번처럼 8 10 12 10 5 를 연주할 때
실제로 외계인처럼 누른다면
현실에선 5 8 10 12 -12 -10 -8 순으로 눌렀다 떼며 답이 7이 된다
하지만 입력 순서상 5는 맨 뒤에 있으므로
8을 입력받는 시점에서 5를 동시에 눌러도 되는지 알 방법이 없다
때문에 컴퓨터적으로 사고하여, 마지막에 5를 추가하여도
앞에서 눌렀던 셈 치는 코드가 필요하다
위 코드는 아래 순서로 스택에 들어간다
<8 10 12 -12 -10 -8 5>

그리고 P의 범위가 300,000 이면서, 시간이 1초이므로
50만줄의 입력을 받으면서 30만줄의 for문을 돌며
다음 프렛을 찾아 인덱스를 1씩 다르게 하면서 탐색하면
아마 시간초과가 날 것이다
어떻게든, 스택에 넣은 값 자체를 특정할 방법이 필요하다
"""