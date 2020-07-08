# Complexities | Time: O(N) | Space: O(N)

def balancedBrackets(string):
    startingBrackets = '{(['
    endingBrackets = '})]'
    bracketsMatching = {
                        '}':'{',
                        ']':'[',
                        ')':'('
                        }
    stack = []
    for char in string:
        if char in startingBrackets:
            stack.append(char)
        elif char in endingBrackets:
            if len(stack) == 0:
                return False
            if stack[-1] == bracketsMatching[char]:
                stack.pop()
            else:
                return False
    return (len(stack) == 0)
