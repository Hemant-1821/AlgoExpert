# Complexities | Time: O(n.d) | Space: O(n+1)
def numberOfWaysToMakeChanges(n , denoms):
    ways = [0] * (n+1)
    ways[0] = 1
    for denom in denoms:
        for amount in range(1,n+1):
            if amount >= denom:
                ways[amount] += ways[amount-denom]
    return ways[n]