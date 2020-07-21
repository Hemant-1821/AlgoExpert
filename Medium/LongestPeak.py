#Complexities Time:O(N) | Space:O(1)
def longestPeak(array):
    longestPeakLength = 0
    i = 1
    while i < len(array) - 1:
        isPeak  = array[i-1] < array[i] and array[i] > array[i+1]
        if not(isPeak):
            i += 1
            continue
        
        leftIdx = i - 2
        rightIdx = i + 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx+1]:
            left -= 1
        while rightIdx < len(array) and array[rightIdx] < array[right -1]:
            rightIdx += 1
        
        currentPeak = rightIdx - leftIdx - 1
        longestPeakLength = max(currentPeak,longestPeakLength)
        i = rightIdx
        
    return longestPeakLength