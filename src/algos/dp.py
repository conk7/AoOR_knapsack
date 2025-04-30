from typing import List


def dp_solution(w: List[int], c: List[int], W: int):
    n = len(w)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    intermediate_steps = 0

    for i in range(1, n + 1):
        for weight in range(W + 1):
            if w[i - 1] <= weight:
                if dp[i - 1][weight] < dp[i - 1][weight - w[i - 1]] + c[i - 1]:
                    dp[i][weight] = dp[i - 1][weight - w[i - 1]] + c[i - 1]
                else:
                    dp[i][weight] = dp[i - 1][weight]
            else:
                dp[i][weight] = dp[i - 1][weight]
            intermediate_steps += 1

    best_weight = max(range(W + 1), key=lambda x: dp[n][x])
    best_value = dp[n][best_weight]

    result_items = [0] * n
    i, current_weight = n, best_weight
    while i > 0 and current_weight >= 0:
        if dp[i][current_weight] != dp[i - 1][current_weight]:
            result_items[i - 1] = 1
            current_weight -= w[i - 1]
        i -= 1

    return result_items, best_value, best_weight, intermediate_steps


__all__ = ["dp_solution"]
