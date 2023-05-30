def solution(babbling):
    ans = 0
    for bab in babbling:
        for speak in ["aya", "ye", "woo", "ma"]:
            if speak * 2 in bab:            # 반복되는게 있으면 말할수없음.
                break
            bab = bab.replace(speak, 'X')   # 말했다는 표시로 'X'한다. 앞 뒤로 같은게 반복될 수 있으니까 '' 빈 문자열이 아닌 것으로 바꿈.
        if bab.count('X') == len(bab):      # 전부 'X'가 되면 ans++
            ans += 1
    return ans
