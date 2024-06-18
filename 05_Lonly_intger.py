def lonelyinteger(a:list):
    # Write your code here
    n = len(a)
    
    for i in a:
        if a.count(i) == 1:
            return i

print(lonelyinteger([1,2,3,4,3,2,1,4,6]))     


