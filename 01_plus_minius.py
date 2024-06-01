def plusMinus(arr):
    # Write your code here
    n = len(arr)
    postive = [i for i in arr if i>0]
    negative =[i for i in arr if i<0] 
    zero=[i for i in arr if i==0]
    pos=len(postive)
    neg=len(negative)
    ze=len(zero)
    print(f'{pos/n:.6f}')
    print(f'{neg/n:.6f}')
    print(f'{ze/n:.6f}')

plusMinus([-4, 3, -9, 0, 4, 1])
