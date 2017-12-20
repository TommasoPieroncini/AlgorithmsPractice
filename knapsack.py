# returns max value achievable with given W = max weight for knapsack,
# given list of weights wt for items
# whose values are in list val
# and quantities in list qnt.
def knapsackDP(W, wt, val, qnt):
    n = len(val)
    tot = sum(qnt)
    K = [[0 for w in range(W + 1)] for i in range(tot + 1)]
    iadj = 0;

    for i in range(1, n + 1):
        for x in range(1, qnt[i - 1] + 1):
            for w in range(1, W + 1):
                if wt[i - 1] <= w:
                    K[iadj + x][w] = max(val[i - 1] + K[iadj + x - 1][w - wt[i - 1]], K[iadj + x - 1][w])
                else:
                    K[iadj + x][w] = K[iadj + x - 1][w]
        iadj = iadj + qnt[i - 1]
        
    return K[tot][W]

# items quantities
qnt = [1, 1, 1, 1]

# items weights
wt = [2, 3, 8, 23]

# items values
val = [1, 4, 5, 6]

# max weight allowed
W = 8
print(knapsackDP(W, wt, val, qnt))
