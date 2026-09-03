def solution(n):
    answer = 0
    n=str(n)
    answer=[int(i) for i in n]
    # print(answer)
    answer.sort(reverse=True)
    # print(answer)
    answer=[str(i) for i in answer]
    # print(answer)
    answer="".join(answer)
    # print(answer)
    answer=int(answer)
    
    return answer