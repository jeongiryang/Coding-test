def solution(x):
    answer = True
    num=x
    
    x=str(x)
    arr_x=[int(i) for i in x]
    print(arr_x)
    
    if num % sum(arr_x) != 0:
        answer=False
    
    return answer