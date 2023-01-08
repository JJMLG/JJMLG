import sys

N, M, R = map(int,input().split())
# print(N,M,R)
A = [list(map(int, input().split())) for _ in range(N)]
numbers = list(map(int, input().split()))
record = [[0]*M for _ in range(N)]

for number in numbers:
    if number == 1:
        if len(A) == M:
            record = [[0] * N for _ in range(M)]
            for i in range(M):
                for j in range(N):
                    # print(A[i][j])
                    record[M - i - 1][j] = A[i][j]
        else:
            record = [[0] * M for _ in range(N)]
            for i in range(N):
                for j in range(M):
                    # print(A[i][j])
                    record[N - i - 1][j] = A[i][j]
        A = record
    elif number == 2:
        if len(A) == M:
            record = [[0] * N for _ in range(M)]
            for i in range(M):
                for j in range(N):
                    record[i][N - j - 1] = A[i][j]
        else:
            record = [[0] * M for _ in range(N)]
            for i in range(N):
                for j in range(M):
                    record[i][M - j - 1] = A[i][j]
        A = record
    elif number == 3:
        # 길이가 M이면
        if len(A) ==M:
            record = [[0] * N for _ in range(M)]
            for i in range(N):
                for j in range(M):
                    record[j][N-i-1] = A[i][j]
            A = record
        elif len(A) ==N:
            record = [[0] * N for _ in range(M)]
            for i in range(N):
                for j in range(M):
                    record[j][N-i-1] = A[i][j]
            A = record
    elif number == 4:
        if len(A) ==N:
            record = [[0] * N for _ in range(M)]
            for i in range(N):
                for j in range(M):
                    record[M - j - 1][i] = A[i][j]
            A = record
        else:
            record = [[0] * M for _ in range(N)]
            for i in range(M):
                for j in range(N):
                    record[N - j - 1][i] = A[i][j]
            A = record
    elif number == 5:
        if len(A) ==N:
            record = [[0] * M for _ in range(N)]
            for i in range(N):
                for j in range(M):
                    # 4분면이면 1로
                    if i< N//2 and j <M//2:
                        record[i][j+M//2]= A[i][j]
                    # 1사분면이면 2사분면으로
                    elif i< N//2 and j >=M//2:
                        record[i+N//2][j]= A[i][j]
                    # 2사분면이면  3사분면으로
                    elif i >= N // 2 and j >= M // 2:
                        record[i][j-M//2]= A[i][j]
                    # 3사분면이면 4사분면으로
                    elif i>=N//2 and j < M//2:
                        record[i-N//2][j] = A[i][j]
        else:
            for i in range(M):
                for j in range(N):
                    # 4분면이면 1로
                    if i< M//2 and j <N//2:
                        record[M][j+N//2]= A[i][j]
                    # 1사분면이면 2사분면으로
                    elif i< M//2 and j >=N//2:
                        record[i+M//2][j]= A[i][j]
                    # 2사분면이면  3사분면으로
                    elif i >= M // 2 and j >= N // 2:
                        record[i][j-N//2]= A[i][j]
                    # 3사분면이면 4사분면으로
                    elif i>=M//2 and j < N//2:
                        record[i-M//2][j] = A[i][j]

            A = record
    else:
        if len(A) ==N:
            record = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                #1사분면이면 4사분면으로
                if i < N // 2 and j >= M // 2:
                    record[i][j-M//2] = A[i][j]
                # 4사분면이면 3사분면으로
                elif i < N // 2 and j < M // 2:
                    record[i+N//2][j] = A[i][j]
                # 3사분면 2사분면
                elif i >= N // 2 and j < M // 2:
                    record[i][j+M//2] = A[i][j]
                #2사분면 1사분면으로
                elif i >= N // 2 and j >= M // 2:
                    record[i-N//2][j] = A[i][j]
        else:
            record = [[0] * N for _ in range(M)]
            for i in range(N):
                for j in range(M):
                    # 1사분면이면 4사분면으로
                    if i < N // 2 and j >= M // 2:
                        record[i][j - M // 2] = A[i][j]
                    # 4사분면이면 3사분면으로
                    elif i < N // 2 and j < M // 2:
                        record[i + N // 2][j] = A[i][j]
                    # 3사분면 2사분면
                    elif i >= N // 2 and j < M // 2:
                        record[i][j + M // 2] = A[i][j]
                    # 2사분면 1사분면으로
                    elif i >= N // 2 and j >= M // 2:
                        record[i - N // 2][j] = A[i][j]
        A = record
print(A)