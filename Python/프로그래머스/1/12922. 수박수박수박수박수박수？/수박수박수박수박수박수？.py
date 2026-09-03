def solution(n):
    answer = '수'*n
    #수수수  
    answer=list(answer)
    print(answer)
    for i in range(n): 
        if i%2!=0: #짝수
            answer[i]='박'
    print(answer)
    answer="".join(answer)
    
    return answer

    # n이 1이면 수,
    # n이 2이면 수박,
    # n이 3이면 수박수,
    # n이 4이면 수박수박
    # n이 5이면 수박수박수