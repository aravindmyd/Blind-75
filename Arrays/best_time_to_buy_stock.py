from typing import List


def best_time_to_buy_stock(prices: List[int]) -> int:
    max_profit: int = 0
    cur_min_price: int = prices[0]

    for price in prices:
        max_profit = max(max_profit, price - cur_min_price)
        if price < cur_min_price:
            cur_min_price = price

    return max_profit


def test_best_time_to_buy_stock():
    assert best_time_to_buy_stock([7, 1, 5, 3, 6, 4]) == 5
    assert best_time_to_buy_stock([7, 6, 4, 3, 1]) == 0


if __name__ == "__main__":
    test_best_time_to_buy_stock()
    print("All test cases passed.")
