def solution(s):
    answer = ''
  
    answer=sorted(s,reverse=True)
    print(str(answer))
    
    return "".join(answer)