def solution(x, n):
    answer = []
    j=x
    for i in range(n):
        answer.append(x)
        x+=j
    print(answer)
    
    
    return answer