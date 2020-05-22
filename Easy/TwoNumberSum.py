'''this algo has Time-O(n) space-O(n)
def twoNumSum(array,targetSum):
    num = {}
    for num in array:
        potentialSum = targetSum-num
        if potentialSum is in num:
            return [potentialSum,num]
        else:
            num[num] = True
    return []
'''
#this will has Time-O(nlogn) Space-O(1)
def twoNumSum(array,targetSum):
    array.sort()
    left = 0
    right = len(array)-1
    while right>left:
        currentSum = array[left]+array[right]
        if currentSum == targetSum:
            return [array[left],array[right]]
        elif currentSum > targetSum:
            right -= 1
        else:
            left += 1
    return []

print(twoNumSum([3,5,-4,8,11,1,-1,6],10))
