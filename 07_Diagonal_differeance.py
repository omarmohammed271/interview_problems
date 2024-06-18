import os
def diagonalDifference(arr):
    x = 0
    a =0
    b = 0
    y = len(arr)-1
    for i in arr:
        a += i[x]
        x +=1
        b += i[y]
        y -=1
    return abs(a-b)  


print(diagonalDifference([[11, 2, 4], 
 [4, 5, 6], 
 [10, 8, -12]]))

