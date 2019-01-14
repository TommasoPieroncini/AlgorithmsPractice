# DP algorithm to solve the Longest Increasing Subsequence problem.
# Input: a sequence of numbers
# Output: a longest increasing subsequence (might not be unique)

def lisDP(mList):
    allSeq = []
    longest = [0, 0]
    for i in range(len(mList) - 1, -1, -1):
        newSeq = [mList[i]]
        maxL = 0
        maxI = -1
        for x in range(i + 1, len(mList)):
            if mList[i] < mList[x] and len(allSeq[(len(mList) - 1) - x]) > maxL:
                maxL = len(allSeq[(len(mList) - 1) - x])
                maxI = (len(mList) - 1) - x
        if maxI != -1:
            newSeq += allSeq[maxI]
        if len(newSeq) > longest[0]:
            longest[0] = len(newSeq)
            longest[1] = len(allSeq)
        allSeq.append(newSeq)
    return allSeq[longest[1]]
        

test = [1,6,7,3,4,47,2,12,3,45,123,563,123]
print(lisDP(test))