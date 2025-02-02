import timeit

        
def find_coins_greedy(coins, sum):
    coins.sort(reverse = True)
    result = {}

    for coin in coins:
        while sum >= coin:
            sum -= coin
            if coin in result:
                result[coin] += 1
            else:
                result[coin] = 1
        if sum == 0:
            return result
    return None

def find_min_coins (coins, sum):
    dp  = [float('inf')]*(sum + 1)
    dp [0] = 0
    used_coins = [0]*(sum + 1)

    for i in range(1, sum + 1 ):
        for coin in coins:
            if coin<= i and dp [i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                used_coins[i] = coin
    result = {}
    curent_sum = sum
    while curent_sum > 0:
        coin = used_coins[curent_sum]
        result[coin] = result.get(coin, 0) + 1
        curent_sum -= coin
    
    return result

coins = list(map(int, input("Введіть номінали монет через пробіл: ").split()))
sum = int(input ("Введіть суму здачі: "))

greedy_time = timeit.timeit(lambda: find_coins_greedy(coins.copy(), sum), number=1)
dp_time = timeit.timeit(lambda: find_min_coins(coins.copy(), sum), number=1)

# Отримуємо результати
greedy_result = find_coins_greedy(coins.copy(), sum)
dp_result = find_min_coins(coins.copy(), sum)

print("\nРезультати:")
print(f"Жадібний алгоритм: {greedy_result}")
print(f"Час виконання жадібного: {greedy_time:.6f} секунд")
print(f"Динамічне програмування: {dp_result}")
print(f"Час виконання ДП: {dp_time:.6f} секунд")

if greedy_result != dp_result and greedy_result is not None and dp_result is not None:
    print("\nУвага: результати відрізняються!")
    greedy_count = sum(greedy_result.values())
    dp_count = sum(dp_result.values())
    print(f"Кількість монет (жадібний): {greedy_count}")
    print(f"Кількість монет (ДП): {dp_count}")



