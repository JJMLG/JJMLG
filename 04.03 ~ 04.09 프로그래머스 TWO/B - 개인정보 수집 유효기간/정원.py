def date_to_days(date):
    year, month, day = map(int, date.split('.'))
    return year*12*28 + month*28 + day

def solution(today, terms, privacies):
    answer = []
    
    today_days = date_to_days(today)
    
    terms_month = {}
    for term in terms:
        term_type, month = term.split()
        terms_month[term_type] = int(month)
        
    i = 0
    for privacy in privacies:
        i += 1
        date, term = privacy.split()
        exp_days = date_to_days(date)
        
        exp_days += terms_month[term]*28 - 1
        
        if exp_days < today_days: # 유효기간 만료
            answer.append(i)
    
    return answer