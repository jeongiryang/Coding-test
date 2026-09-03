def solution(a, b):
    answer = 1234567890
    
    result=0
    for i,j in zip(a,b):
        result+= i*j
    answer=result    
    
    return answer