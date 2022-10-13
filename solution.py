def diagonalDifference(arr):
    
    length = len(arr)
    
    left_right = 0
    right_left = 0
    
    for i in range(length):
        left_right += arr[i][i]
    
    back = -1
    
    for j in range(length):
        right_left += arr[j][back]
        back -= 1
    
    return abs(left_right - right_left)
