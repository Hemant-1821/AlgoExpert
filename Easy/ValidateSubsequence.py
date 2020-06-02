# Complexities | Time: O(N) | Space: O(1)

def validateSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)

print(validateSubsequence([5,1,22,25,6,-1,8,10], [1,6,-1,10]))

