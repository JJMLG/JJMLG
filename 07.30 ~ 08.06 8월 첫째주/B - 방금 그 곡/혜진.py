def changeInfo(info):           # 헷갈리지 않게 두개짜리 하나로 변경
    info = info.replace('A#', 'a')
    info = info.replace('C#', 'c')
    info = info.replace('D#', 'd')
    info = info.replace('F#', 'f')
    info = info.replace('G#', 'g')
    return info

def solution(m, musicinfos):
    m = changeInfo(m)
    ans = []
    for i in range(len(musicinfos)):
        st, ed, title, info = musicinfos[i].split(',')
        info = changeInfo(info)
        
        hour, minute = map(int, st.split(':'))
        st = hour * 60 + minute # 시간은 분으로 변경
        
        hour, minute = map(int, ed.split(':'))
        ed = hour * 60 + minute
        
        dt = ed - st            # 재생 시간(분)

        while len(info) < dt:   # 재생 시간만큼 반복 재생
            info += info
        info = info[:dt]
        
        if m in info:           # 들은 멜로디가 있으면
            ans.append([title, dt, i])      # 제목, 재생시간, 입력된 순서

    if not ans:
        return '(None)'
    ans.sort(key=lambda x: (-x[1], x[2]))   # 재생시간 내림차순, 입력된 순서 오름차순 정렬
    return ans[0][0]
