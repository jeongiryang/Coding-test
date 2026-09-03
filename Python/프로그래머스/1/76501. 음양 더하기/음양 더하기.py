def solution(absolutes, signs):
    answer = 123456789
    sum=0
    for j,i in zip(absolutes,signs):
        if i!=True:
            j=-1*j
        sum+=j
    
    answer=sum
    return answer