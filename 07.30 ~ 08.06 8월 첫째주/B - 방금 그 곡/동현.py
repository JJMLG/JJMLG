def solution(m, musicinfos):
    answer = ''
    m = m.replace("C#","Q").replace("D#","W").replace("F#","I").replace("G#","R").replace("A#","T").replace("E#","Y")
    result = []
    for music in musicinfos:
        splited = music.split(",")
        
        splited[3] = splited[3].replace("C#","Q").replace("D#","W").replace("F#","I").replace("G#","R").replace("A#","T").replace("E#","Y")
        if splited[1] == "00:00":
            splited[1] == "24:00"
        times = (int(splited[1].split(":")[0]) - int(splited[0].split(":")[0]))*60 + int(splited[1].split(":")[1]) - int(splited[0].split(":")[1])
        print(times)
        text = ""
        for i in range(times):
            text += splited[3][i%len(splited[3])]
        if m in text:
            result.append([splited[2],times,len(splited[2])])
    
    if result == []:
        return "(None)"
    else:
        print(result)
        temp = []
        maxx = 0
        ans = ""
        for i in range(len(result)):
            if result[i][1] > maxx:
                temp = []
                maxx = result[i][1]
                ans = result[i][0]
        return ans
                
            
        
                
        # return result[idx][0]
    
    # return answer