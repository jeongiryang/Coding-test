def solution(left, right):
    answer = 0
    sum=0
    count=0
    for i in range(left,right+1):
        for j in range(1,i+1):
            if i%j==0:
                count+=1 
        if count % 2==0:
            sum+=i
        else:
            sum-=i
        count=0
        
    answer=sum
    return answer