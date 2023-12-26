coins = (1, 2, 5, 10, 25, 50)


def find_coins_greedy(amount):
    coin_counts = {}

    for coin in sorted(coins, reverse=True):
        while amount >= coin:
            if coin not in coin_counts:
                coin_counts[coin] = 0
            coin_counts[coin] += 1
            amount -= coin

    return {k: v for k, v in coin_counts.items() if v > 0}


def find_min_coins(amount):
    max_coins = amount // min(coins)

    min_coins = [max_coins] * (amount + 1)
    min_coins[0] = 0

    selected_coins = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                selected_coins[i] = coin

    if min_coins[amount] == max_coins:
        max_possible_amount = max(i for i in range(amount + 1) if min_coins[i] != max_coins)
        return get_coins(max_possible_amount, selected_coins)

    return get_coins(amount, selected_coins)


def get_coins(amount, selected_coins):
    coin_counts = {}
    while amount > 0:
        coin = selected_coins[amount]
        if coin in coin_counts:
            coin_counts[coin] += 1
        else:
            coin_counts[coin] = 1
        amount -= coin
    return coin_counts


def check_amount(coin_counts):
    amount = 0

    for coin, count in coin_counts.items():
        amount += coin * count

    return amount


def main():
    global coins
    coins = (2, 5, 10, 25, 50)

    amount = 113

    print("\nGreedy algorithm:")
    greedy_coins = find_coins_greedy(amount)
    print(f"Coins: {greedy_coins}; Amount: {check_amount(greedy_coins)}")

    print("\nDynamic programming:")
    dynamic_coins = find_min_coins(amount)
    print(f"Coins: {dynamic_coins}; Amount: {check_amount(dynamic_coins)}")


if __name__ == "__main__":
    main()
