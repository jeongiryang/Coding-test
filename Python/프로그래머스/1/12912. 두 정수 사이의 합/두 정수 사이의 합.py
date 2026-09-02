def solution(a, b):
    answer=0
    if a==b:
        return a
    for i in range(abs(a-b)+1):
        if a<b:
            answer+=a
            a+=1
        else:
            answer+=a
            a-=1

    return answer