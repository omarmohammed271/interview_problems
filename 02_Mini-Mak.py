
def miniMaxSum(arr:list):
    # Write your code here
    n = len(arr)
    arr.sort()
    arr_min = arr[:n-1]
    arr_max = arr[1:]
    print(sum(arr_min),sum(arr_max))
 

miniMaxSum([1,2,5,4,3])