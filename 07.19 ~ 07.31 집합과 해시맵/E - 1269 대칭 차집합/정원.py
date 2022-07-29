A, B = map(int, input().split())
A_list = list(map(int, input().split()))
A_set = set(A_list)
B_list = list(map(int, input().split()))
B_set = set(B_list)
result = []
for a in A_list:
    if a not in B_set:
        result.append(a)
for b in B_list:
    if b not in A_set:
        result.append(b)
print(len(result))

"""
A_list와 A_set의 원소는 같음
다만 교집합 여부 확인 시, 
in을 사용할 때 list보다 빠르게 확인하기 위해 set을 사용함
"""