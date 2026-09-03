from collections import Counter
def solution(s):
    answer = True
    howmany_p=s.count('p')+s.count('P')
    howmany_y=s.count('y')+s.count('Y') 
    

    if howmany_p!=howmany_y:
        answer=False
      
    return answer
    # s = s.lower()
    # count_list = Counter(s)
    # print(count_list)
    
    # return count_list["p"] == count_list["y"]


