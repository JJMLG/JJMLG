import sys
input = sys.stdin.readline                  # 이거 하고 pypy로 해야 성공

S = input()
q = int(input())

# k: 알파벳, v: 해당 idx까지 몇번 나왔나 -> 배열
dic = {}

for _ in range(q):
    a, l, r = input().split()
    if a in dic:                            # 알파벳이 나온적이 있으면 배열이 이미 존재함
        arr = dic[a]
    else:
        prev = 0
        arr = [0] * len(S)                  # 처음 나온 알파벳은 배열 만들기
        for i in range(len(S)):
            if S[i] == a:                   # 알파벳 나왔으면 +1
                prev += 1
            arr[i] = prev                   # 누적합으로 구하는거니까 안나와도 배열에 prev 넣기
        dic[a] = arr                        # 배열 완성되면 dict에 넣기

    if l == '0':                            # 처음부터 시작이면 뺄 필요 없음
        print(arr[int(r)])
    else:                                   # 중간부터면 앞부분은 빼주기
        print(arr[int(r)] - arr[int(l)-1])
