
def bubbleSort(array):
    isSorted = False
    count = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - count):
            if array[i+1] > array[i]:
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] = temp
                isSorted = False
        count += 1
    return array