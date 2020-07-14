#(M-1)Complexities(Both) Time: O(N) | Space: O(1)
def MonotonicArr(li):
    i = 0
    dec = False
    inc = False
    if li[i] == li[i+1]:
        while li[i] == li[i+1]:
            i += 1
    if li[i] > li[i+1]:
        dec = True
        inc = False
    else:
        inc = True
        dec = False
        
    flag = True
    while flag and i<(len(li)-1):
        if li[i] > li[i+1]:
            if dec:
                i += 1
                continue
            else:
                flag = False
                break
        elif li[i] < li[i+1]:
            if inc:
                i += 1
                continue
            else:
                flag = False
                break
        else:
            i += 1
            continue
        
    print(flag)

#(M-2)
def MonotonicArr(li):
    isNonInc = True
    isNonDec = True
    for i in range(1,len(li)):
        if li[i] < li[i-1]:
            isNonDec = False
        if li[i] > li[i-1]:
            isNonInc - False
    return isNonDec or isNonInc
