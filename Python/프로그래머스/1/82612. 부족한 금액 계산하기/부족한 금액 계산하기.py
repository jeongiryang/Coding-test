def solution(price, money, count):
    result= 0
    tmp=price
    
    for i in range(1,count+1):
        price=tmp
        price*=i
        result+=price
    
    answer=result-money
    if answer<=0:
        answer=0
        
    
    
    return answer