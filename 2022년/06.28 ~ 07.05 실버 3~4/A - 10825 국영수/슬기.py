import sys
sys.stdin = open('input.txt')

grade = int(input())

arr = []

for _ in range(grade):
    name, korean, english, math = input().split()
    arr.append([name, int(korean), int(english), int(math)])

# 국어, 영어, 수학, 이름 순으로 정렬 (문자는 str붙여서 정렬)
order_arr = sorted(arr, key=lambda x: (-x[1], x[2], -x[3], str(x[0])))
print(order_arr)


for i in range(grade):
    print(order_arr[i][0])