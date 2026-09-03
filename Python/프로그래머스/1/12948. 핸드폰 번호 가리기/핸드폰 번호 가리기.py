def solution(phone_number):
    answer = ''
    
    show_number=phone_number[-4:]
    #print(show_number)
    
    how_many_star=len(phone_number)-len(show_number)
    
    answer=how_many_star*"*"+show_number
    
    
    return answer