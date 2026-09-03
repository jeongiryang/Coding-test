def solution(n):
    answer = 0
    x=[]
    for i in range(n):
       if n%(i+1)==1:
            x.append(i+1)
    answer=min(x)
        
    return answer