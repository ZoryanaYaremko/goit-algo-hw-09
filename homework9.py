def find_coins_greedy(amount, coins):
    """Жадібний алгоритм для визначення кількості монет кожного номіналу."""
    coins_count = {}
    
    for coin in coins:
        count = amount // coin
        if count > 0:
            coins_count[coin] = count
        amount -= coin * count
    
    return coins_count


def find_min_coins(amount, coins):
    """Алгоритм динамічного програмування для визначення мінімальної кількості монет."""
    # Ініціалізація таблиці для зберігання мінімальної кількості монет для кожної суми
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Для суми 0 потрібно 0 монет
    
    # Ініціалізація списку для відновлення рішення
    coin_used = [-1] * (amount + 1)
    
    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin
    
    # Відновлення рішення
    if dp[amount] == float('inf'):
        return {}
    
    coins_count = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in coins_count:
            coins_count[coin] += 1
        else:
            coins_count[coin] = 1
        amount -= coin
    
    return coins_count


if __name__ == '__main__':
    coins = [50, 25, 10, 5, 2, 1]
    amount = 137

    print("Жадібний алгоритм:")
    print(find_coins_greedy(amount, coins))

    print("\nДинамічне програмування:")
    print(find_min_coins(amount, coins))
    
    # Вимірювання часу виконання
    import time

amount = 543210

start_time = time.time()
find_coins_greedy(amount, coins)
print(f"Greedy Algorithm took {time.time() - start_time:.6f} seconds")

start_time = time.time()
find_min_coins(amount, coins)
print(f"Dynamic Programming took {time.time() - start_time:.6f} seconds")

