def headNumIdx(file, idx):                  # HEAD, NUMBER, INDEX를 반환하는 함수
    h = n = ''
    i = 0
    while i < len(file):
        if file[i].isdigit(): break
        h += file[i]
        i += 1
    while i < len(file):
        if len(n) == 5: break
        if not file[i].isdigit(): break
        n += file[i]
        i += 1
    return [h.lower(), int(n), idx]
    

def solution(files):
    origin = files[::]                      # 출력을 위해 원래 값 보존
    for i in range(len(files)):
        files[i] = headNumIdx(files[i], i)  # 정렬을 위해 HEAD, NUMBER, INDEX를 가져온다
    files.sort()
    return [origin[f[2]] for f in files]    # f[2]가 원래 index임
