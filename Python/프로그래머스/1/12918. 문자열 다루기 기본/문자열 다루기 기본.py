def solution(s):
    answer=True
    s=list(s)
    
    if len(s)==4 or len(s)==6:
        for i in range(len(s)):
            if s[i].isdigit():
                s[i]=True
            else:
                s[i]=False
    else:
        answer=False    
    print(s)
    
    if False in s:
        answer=False
        
    return answer