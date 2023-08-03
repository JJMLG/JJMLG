def changeInfo(info):
    info = info.replace('A#', 'a')
    info = info.replace('C#', 'c')
    info = info.replace('D#', 'd')
    info = info.replace('F#', 'f')
    info = info.replace('G#', 'g')
    return info

def solution(m, musicinfos):
    m = changeInfo(m)
    N = len(musicinfos)
    ans = []
    for i in range(N):
        st, ed, title, info = musicinfos[i].split(',')
        info = changeInfo(info)
        
        hour, minute = map(int, st.split(':'))
        st = hour * 60 + minute
        
        hour, minute = map(int, ed.split(':'))
        ed = hour * 60 + minute
        
        dt = ed - st  # 재생 시간(분)

        while len(info) < dt:
            info += info
        info = info[:dt]
        
        if m in info:
            ans.append([title, dt, i])

    if not ans:
        return '(None)'
    ans.sort(key=lambda x: (-x[1], x[2]))
    return ans[0][0]
