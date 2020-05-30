#Recursive
#Complexities time: O(log(N)) | space: O(log(N))

def BinarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)

def binarySearchHelper(array, target, left, right):
    if left>right:
        return -1
    middle = (left+right)//2
    potentialTarget = array[middle]

    if target > potentialTarget:
        binarySearchHelper(array, target, middle+1, right)
    elif target < potentialTarget:
        binarySearchHelper(array, target, array, middle-1)
    else:
        return middle

#Iterative
#Complexities time: O(log(N)) | space: O(1)

def BinarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)

def binarySearchHelper(array, target, left, right):
    while left <= right:
        middle = (left+right)//2
        potentialTarget = array[middle]
        if target > potentialTarget:
            left = middle + 1
        elif target < potentialTarget:
            right = middle - 1
        else:
            return middle
    return -1