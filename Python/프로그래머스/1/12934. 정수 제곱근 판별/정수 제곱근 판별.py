import math

def solution(n):
    answer = 0
    n=math.sqrt(n)
    
    what_is_n=n.is_integer()
    
    if what_is_n:
        answer=(n+1)**2
    else:
        answer=-1
    
    return answer