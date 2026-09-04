def solution(arr1, arr2):
    answer = []
    length_row=len(arr1)
    length_col=len(arr1[0])
    
    for i in range(length_row):
        answer.append([])
        for j in range(length_col):
            answer[i].append(arr1[i][j]+arr2[i][j])
 
       
    return answer