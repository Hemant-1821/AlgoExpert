#Mehtod:1 | Iterative | Time: O(N) | Space: O(H) H: Height of the Binary Tree

def nodeDepths(root):
    sumOfDepths = 0
    stack = [{"node":root, "depth": 0}]
    while len(stack) > 0:
        nodeInfo = stack.pop()
        Node, depth = nodeInfo["node"],nodeInfo["depth"]
        if Node is None:
            continue
        sumOfDepths += depth
        stack.append({"node":Node.left, "depth":depth+1})
        stack.append({"node":Node.left, "depth":depth+1})

#Method:2 | Recursive | Time: O(N) | Space: O(H)

def nodeDepths(node, depth = 0):
    if node is None:
        return 0
    return depth + nodeDepths(node.left, depth+1) + nodeDepths(node.right, depth+1)