#complexities
#Time = O(N) N is the total number of int elements in initial array
#Space = O(Depth)

def ProductSum(Arr):
    print(CalculateProductSum(Arr,0,1))

def CalculateProductSum(Arr,sum,depth):
    for i in Arr:
        if type(i) is list:
            sum = sum + CalculateProductSum(i,0,depth+1)
        else:
            sum = sum + i
    return sum * depth

ProductSum([1,2,[3,4],[5,[6,7],8]])