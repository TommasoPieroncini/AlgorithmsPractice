phoneDict = {
    1: ['a','b','c'],
    2: ['d', 'e', 'f'],
    3: ['g', 'h', 'i'],
    4: ['j', 'k', 'l'],
    5: ['m', 'n', 'o'],
    6: ['p', 'q', 'r'],
    7: ['s', 't', 'u'],
    8: ['v', 'w', 'x'],
    9: ['y', 'z', '#'],
    0: ['@', '_', '%']
}

def makeCombos(number, mDict):
    combos = []
    numStr = str(number)
    result = ""
    stack = []
    stack.append(result)
    while not len(stack) == 0:
        result = stack.pop()
        d = len(result) 
        if len(result) == len(numStr):
            combos.append(result)
        else:
            for l in mDict[int(numStr[d])]:
                stack.append(result + l)
    return combos

print makeCombos("56083312", phoneDict)