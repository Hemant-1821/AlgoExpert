def smallDiff(arrOne,arrTwo):
    arrOne.sort()
    arrTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float('inf')
    current = float('inf')
    smallestPair = []
    while idxOne < len(arrOne) and idxTwo < len(arrTwo):
        firstNum = arrOne[idxOne]
        secondNum = arrTwo[idxTwo]
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif firstNum > secondNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]

        if current < smallest:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair

print(smallDiff([-1,5,10,20,28,3], [26,134,135,15,27]))