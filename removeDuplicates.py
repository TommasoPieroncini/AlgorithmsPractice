x = "31312366"

def removeDuplicates(mStr):
    strList = [mStr[i] for i in range(len(mStr))]
    mSet = set()
    count = 0
    while i < len(mStr):
        if strList[i] in mSet:
            count += 1
            strList.append(strList.pop(i))
            i -= 1
        else:
            mSet.add(strList[i])
            i += 1
    return ''.join(strList[:])
        
print removeDuplicates(x)