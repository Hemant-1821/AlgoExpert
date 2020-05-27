# METHOD 1 Recursive 
#complexities:
#Average: Time - O(log(N)) | Space - O(log(N))
#Worst: Time - O(N) | Space - O(log(N))
"""
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))

def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = abs(target - tree.value)
    if target > tree.value:
        return findClosestValueInBstHelper(tree.right,target,closest)
    elif target < tree.value:
        return findClosestValueInBstHelper(tree.left,target,closest)
    else:
        return closest
"""

# METHOD 2 Iterative (BEST)
#complexities:
#Average: Time - O(log(N)) | Space - O(1)
#Worst: Time - O(N) | Space - O(1)

def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))

def findClosestValueInBstHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = abs(target - tree.value)
        if target > currentNode.value:
            currentNode = currentNode.right
        elif target < currentNode.value:
            currentNode = currentNode.left
        else:
            break
    return closest