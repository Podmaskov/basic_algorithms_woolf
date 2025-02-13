def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [(float('inf'), None)] * (amount + 1)
    dp[0] = (0, 0)

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin][0] + 1 < dp[i][0]:
                dp[i] = (dp[i - coin][0] + 1, coin)

    coin_usage = {}
    remaining = amount
    while remaining > 0:
        coin = dp[remaining][1]
        if coin is None:
            break
        coin_usage[coin] = coin_usage.get(coin, 0) + 1
        remaining -= coin
    return coin_usage

if __name__ == "__main__":
    test_amount = 113
    print("Greedy Algorithm:", find_coins_greedy(test_amount))
    print("Dynamic Programming:", find_min_coins(test_amount))