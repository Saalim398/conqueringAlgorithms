#Knapsack Algorithmṇ
def knapsackRec(W, val, wt, n):

    # Base Case
    if n == 0 or W == 0:
        return 0

    pick = 0


    if wt[n - 1] <= W:
        pick = val[n - 1] + knapsackRec(W - wt[n - 1], val, wt, n - 1)
    
    
    notPick = knapsackRec(W, val, wt, n - 1)
     
    return max(pick, notPick)

def knapsack(W, val, wt):
    n = len(val)
    return knapsackRec(W, val, wt, n)


val = [1, 2, 3]
wt = [4, 5, 1]
W = 4

print(knapsack(W, val, wt))