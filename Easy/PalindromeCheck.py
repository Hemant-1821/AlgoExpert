# Method-1 | Time: O(n^2) | Space: O(n)

def isPalindrome(string):
    reversedString = ''
    for i in reversed(range(0,len(string))):
        reversedString += string[i]
    return string == reversedString

# Method-2 | Time: O(N) | Space: O(N)

def isPalindrome(string):
    reversedChar = []
    for i in reversed(range(0,len(string))):
        reversedChar.append(string[i])
    return string == "".join(reversedChar)

# Method-3(Recursive) | Time: O(N) | Space: O(N)

def isPalindrome(string,i=0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome(string ,i+1)

#tail recursion(Will optimize it slightly but it totally depends on compiler)
def isPalindrome(string,i=0):
    j = len(string) - 1 - i
    if i >= j:
        return True
    if string[i] != string[j]:
        return False
    return isPalindrome(string ,i+1)

# Method-4(Iterative) | Time: O(N) | Space: O(1)
#BEST
def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True
        
