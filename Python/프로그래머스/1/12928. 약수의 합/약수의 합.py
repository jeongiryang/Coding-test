def solution(n):
    N=n+1
    sum=0
    for i in range(1,N):
        if n%i==0:
            sum+=i
    return sum