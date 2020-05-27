class BST:

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

# Average: Time - O(logn) space - O(1)
# Worst: Time - O(n) space - O(1)
    def insert(self, value):
        currentNode = self
        while True:
            if value > currentNode.value:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right

            else:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            
            return self #this will help while chaining the insert statements

# Average: Time - O(logn) space - O(1)
# Worst: Time - O(n) space - O(1)
    def containes(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False

# Average: Time - O(logn) space - O(1)
# Worst: Time - O(n) space - O(1)
    def remove(self, value, parentNode = None):
        currentNode = self
        while True:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value,currentNode)
                # root node with on child only
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.left = currentNode.left.left
                        currentNode.right = currentNode.left.right

                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right

                    else:
                        currentNode.value = None

                elif parentNode.left == currentNode:
                    currentNode = currentNode.left if currentNode.left is not None else currentNode.right

                elif parentNode.right == currentNode:
                    currentNode = currentNode.left if currentNode.left is not None else currentNode.right
                break
        return self

        def getMinValue(self):
            currentNode = self
            while currentNode.left is not None:
                currentNode = currentNode.left

            return currentNode.value