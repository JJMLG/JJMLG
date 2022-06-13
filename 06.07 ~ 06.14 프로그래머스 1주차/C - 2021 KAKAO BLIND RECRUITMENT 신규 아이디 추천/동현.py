import re

def solution(new_id):
    answer = ''
    step1 = new_id.lower()
    step2 = re.sub(r'[^0-9-_a-z.]',"",step1)
    step3 = re.sub('\.+','.',step2)
    step4 = step3.strip('.')
    if step4 == "":
        step4 = "a"
    if len(step4) >= 16:
        step4 = step4[:15].strip('.')
    if len(step4) <= 2:

        while len(step4) != 3:
            step4 = step4 + step4[-1]
      
    answer = step4
    return answer