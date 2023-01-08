import sys
sys.stdin = open("10162.txt")

# 1.큰 수부터 나누고 몫 a횟수 나머지를 b로나누고 c로 나누어서 a+b+c
# 2. 각각a, 각b, 각c 1씩 증가하면서 값이 100되면 min에 담고 다음 min이랑 또 비교해서 젤 작은거 출력

#1번으로 먼저

# 요리시간 입력
T = int(input())

a = 60 *5
b = 60
c = 10

result = []
a_number = 0
b_number=0
c_number=0
x = 0
while T:
    a_number = T//a
    b_number = T % a // b
    c_number = ((T % a) % b) // c
    if ((T % a) % b) % c == 0:
        result.append(a_number)
        result.append(b_number)
        result.append(c_number)
        break
    else:
        print(-1)
        break
print(*result)
