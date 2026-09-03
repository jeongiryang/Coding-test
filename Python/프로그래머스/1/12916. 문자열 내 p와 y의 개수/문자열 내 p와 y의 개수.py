def solution(s):
    answer = True
    howmany_p=s.count('p')+s.count('P')
    howmany_y=s.count('y')+s.count('Y') 
    

    if howmany_p!=howmany_y:
        answer=False
    
    return answer