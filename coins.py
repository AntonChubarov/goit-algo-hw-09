denominations = (5, 10, 25, 50)

def find_coins_greedy(amount: int) -> dict:
    coin_counts = {}

    for denom in sorted(denominations, reverse=True):
        while amount >= denom:
            if denom not in coin_counts:
                coin_counts[denom] = 0
            coin_counts[denom] += 1
            amount -= denom

    return {k: v for k, v in coin_counts.items() if v > 0}


def find_min_coins(amount: int) -> dict[int, int]:
    coin_counts = {denom: 0 for denom in denominations}
    min_coins = [0] + [amount//min(denominations)+1] * amount
    last_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for denom in denominations:
            if denom <= i and min_coins[i - denom] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - denom] + 1
                last_used[i] = denom

    while amount >= min(denominations):
        coin_counts[last_used[amount]] += 1
        amount -= last_used[amount]

    coin_counts = {k: v for k, v in sorted(coin_counts.items(), reverse=True)}
    return {k: v for k, v in coin_counts.items() if v > 0}

def main():
    amount = 113
    print(find_coins_greedy(amount))
    print(find_min_coins(amount))

if __name__ == "__main__":
    main()
