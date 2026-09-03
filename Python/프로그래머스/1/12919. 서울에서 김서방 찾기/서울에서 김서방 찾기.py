def solution(seoul):
    answer = ''
    n=0
    
    for where, result in enumerate(seoul):
        if result=='Kim':
            n=where
    answer+=f"김서방은 {n}에 있다"
    
    return answer