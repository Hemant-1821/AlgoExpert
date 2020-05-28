class BinaryTree:

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

#Complexities:
#Time : O(N)
#Space : O(log(N))

def BranchSums(root):
    sums = []
    CalculateBranchSums(root, 0, sums)
    return sums

def CalculateBranchSums(node, runningSums, sums):
    if node is None:
        return 
    runningSums += node.value
    if node.left is None and node.right is None:
        sums.append(runningSums)
        return

    CalculateBranchSums(node.left, runningSums, sums)
    CalculateBranchSums(node.right, runningSums, sums)
