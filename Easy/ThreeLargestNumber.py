def ThreeLargestNumber(array):
    threeLargest = [None, None, None]
    for num in array:
        updateLargestThree(threeLargest, num)
    return threeLargest


def updateLargestThree(threeLargest ,num):
    if threeLargest[2] is None or num > threeLargest[2]:
        updateAndShift(num, threeLargest, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        updateAndShift(num, threeLargest, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        updateAndShift(num, threeLargest, 0)

def updateAndShift(num, threeLargest, index):
    for i in range(index+1):
        if i == index:
            threeLargest[i] == num
        else:
            threeLargest[i] = threeLargest[i+1]