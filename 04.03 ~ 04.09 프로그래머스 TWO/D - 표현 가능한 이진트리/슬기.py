import math

def check(num_bin, prev_parent):
    # 중앙값(자손) 기준으로 재귀적으로 확인
    mid = len(num_bin) // 2
    if num_bin:
        son = (num_bin[mid] == '1')
    else:
        return True

    # 내가 존재하면 부모가 존재해야함.
    if son and not prev_parent:
        return False
    else:
        return check(num_bin[mid + 1:], son) and check(num_bin[:mid], son)


def sol(num):
    # 1은 항상 참
    if num == 1: return 1

    # 2진수 변환
    num_bin = bin(num)[2:]
    # 2^n - 1꼴의 자릿수를 가져야함.
    digit = 2 ** (int(math.log(len(num_bin), 2)) + 1) - 1
    num_bin = "0" * (digit - len(num_bin)) + num_bin
    # print(digit, num_bin)

    # 누군가의 부모 노드는 항상 존재해야함.
    if num_bin[len(num_bin) // 2] == '1' and check(num_bin, True):
        return 1
    else:
        return 0


def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(sol(num))
    return answer