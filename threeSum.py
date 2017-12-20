def threeSum(mList, target):
    results = []
    mList = sorted(mList)
    for i in range(len(mList)):
        a = mList[i]
        start = i + 1
        end = len(mList) - 1
        while start < end:
            b = mList[start]
            c = mList[end]

            if a + b + c == target:
                results.append((a, b, c))
                if b == mList[start + 1]:
                    start = start + 1
                else:
                    end = end - 1
                
            elif a + b + c > target:
                end = end - 1
            else:
                start = start + 1
    return results

print threeSum([0, 2, 2, 3, 23, 64, 12, 32, 10, 2], 5)
