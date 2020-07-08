# Complexities Time: O(N^2) | Space: O(1)

def LongestPalindromeSubstring(string):
    currentLongest = [0,1]
    for i in range(len(string)):
        odd = getLongestPalindrome(string, i - 1, i + 1)
        even = getLongestPalindrome(string, i - 1, i)
        longest = max(odd, even, key = lambda x: x[1] - x[0])
        currentLongest = max(currentLongest ,longest, key = lambda x: x[1] - x[0])
    return string[currentLongest[0]:currentLongest[1]]

def getLongestPalindrome(string, leftIdx, rightIdx):
    while leftIdx > 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    return [leftIdx+1, rightIdx]

