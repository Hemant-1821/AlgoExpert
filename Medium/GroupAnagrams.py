#Complexities: Space:O(N.W) | Time:O(W.N(Log(N)))

def groupAnagrams(array):
    auxArr = []
    for i in array:
        temp = sorted(i)
        auxArr.append("".join(temp))
    ana_dict = {}
    for i in range(len(array)):
        if auxArr[i] in ana_dict:
            ana_dict[auxArr[i]].append(array[i])
        else:
            ana_dict[auxArr[i]] = [array[i]]
    print(ana_dict)
    
groupAnagrams(['yo','act','flop','tac','cat','oy','olfp'])
