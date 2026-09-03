def solution(num):
    i=0
    
    while (num!=1):
        if num %2==0:
              num//=2
              i+=1
        else:
              num=num*3+1
              i+=1
        if i==500:
            i=-1
            break
       
    return i