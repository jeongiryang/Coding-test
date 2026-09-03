def solution(arr):
    answer = arr
    
    smallest=min(arr)
    arr.remove(smallest)
    
    
    
    if not answer:
        answer=[-1]

    
    return answer