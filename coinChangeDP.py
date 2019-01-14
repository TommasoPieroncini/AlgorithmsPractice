amount = 1000000
denominations = [5, 10, 25, 50]

def coinChange(amount, denominations):
    matrix = [[0 for i in range(len(denominations) + 1)] for x in range(amount + 1)]

    matrix[0] = [1 for i in range(len(denominations) + 1)]

    for i in range(1,amount + 1):
        for j in range(len(denominations)):
            if i - denominations[j] >= 0 and j > 0:
                matrix[i][j] = matrix[i-denominations[j]][j] + matrix[i][j-1]
            elif j > 0:
                matrix[i][j] = matrix[i][j-1]
            elif i - denominations[j] >= 0:
                matrix[i][j] = matrix[i-denominations[j]][j]
    
    return matrix[amount][len(denominations)-1]

print coinChange(amount, denominations)