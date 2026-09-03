def solution(s):
    answer = ''
    
    how_many=len(s)
    even_num=0
    odd_num=0
   
    #abcde
    #qwer
    #abcdefg
    #qwerqwer
    if how_many % 2==1:  #단어의 길이가 홀수
        even_num=how_many//2+1
        answer=s[even_num-1]
    else:
        odd_num=how_many//2  #단어의 길이가 짝수
        answer=s[odd_num-1]+s[odd_num]
    
   
    return answer