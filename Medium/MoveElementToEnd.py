#Complexities : Time: O(N) | Space: O(1)
def MoveElementToEnd(li, target):
    left = 0
    right = len(li)-1
    if li[right] == target:
        while li[right] == target:
            right -= 1
    while left < right:
        if li[left] == target:
            li[left],li[right] = li[right],li[left]
            right -= 1
        left += 1
    return li

print(MoveElementToEnd([2,1,2,2,2,3,4,2],2))
        