def coin_change_ways_recursive(coins, s):
    return _coin_change_ways_recursive(coins, s)


def _coin_change_ways_recursive(coins, s):
    if s == 0:
        return 1

    if len(coins) == 0 or s < 0:
        return 0

    return _coin_change_ways_recursive(coins[1:], s) \
        + _coin_change_ways_recursive(coins, s-coins[0])


def coin_change_ways_dynamic1(coins, s):
    x = [[0 for _ in range(s+1)] for i in range(len(coins)+1)]
    for i in range(1, len(coins)+1):
        x[i][0] = 1

    for i in range(1, len(coins)+1):
        for j in range(1, s+1):
            if coins[i-1] < j:
                x[i][j] = x[i][j-1]
            else:
                x[i][j] = x[i-1][j] + x[i][j-coins[i-1]]

    return x[-1][-1]
