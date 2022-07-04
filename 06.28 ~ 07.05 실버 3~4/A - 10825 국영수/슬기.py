import sys
sys.stdin = open('input.txt')

grade = int(input())

# arr = [input().split() for _ in range(grade)]
# print(arr)
arr = []

for _ in range(grade):
    name, korean, english, math = input().split()
    # print(name, korean, english, math)
    arr.append([name, int(korean), int(english), int(math)])
# print(arr)

# print(sorted(arr, key=lambda x: (-x[1], x[2], -x[3], x[0)))
# name_order = arr[0]
# max_korean = int(arr[1])
# min_english = int(arr[2])
# max_math = int(arr[3])

order_arr = sorted(arr, key=lambda x: (-x[1], x[2], -x[3], str(x[0])))
print(order_arr)

for i in range(grade):
    print(order_arr[i][0])



# for i in range(grade):
#     if max_korean <= int(arr[i][1]):
#         arr[i] = arr[i]


"""
국어 점수가 감소하는 순서로 > 큰거 에서 작은걸로
국어 점수가 같으면 영어 점수가 증가하는 순서로
국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)
"""