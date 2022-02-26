import sys
sys.stdin = open('1969.txt')

N, M = map(int, input().split())
DNA = [list(input()) for _ in range(N)]
# print(DNA)
temp_count = 0
# print(temp)
# 최종적으로 나올 염기서열
result =""
final_count = 0
final_S=''
temp_S = ""
minn = N
# 사전순으로 빠른 것부터 출력해야하므로 acgt 순으로
mat= ['A', "C", "G", 'T']
for j in range(M):
    minn = N
    temp_S =""
    for word in mat:
        temp_count = 0
        for i in range(N):
            # 세로로 한줄씩 word랑 다르면 count
            if word != DNA[i][j]:
                temp_count+=1
        # 얼마나 다른지 세서 min값보다 작으면 temp_count가 min값이고 temp_s가 해당 단어로
        # 위에서 사전순으로 배치했기 때문에 같지 않고 작을 때만 바꿔주는걸로
        if temp_count < minn:
            minn = temp_count
            temp_S = word
    # 만약 temp_count가 가장 적은 단어에 해당하면
    final_count +=minn
    final_S +=temp_S
print(final_S)
print(final_count)
