import math
from typing import List
from .two_approx import two_approx_solution


def fptas_solution(w: List[int], c: List[int], W: int, epsilon: float = 0.1):
    n = len(w)
    intermediate_steps = 0

    _, tas_total_val, _, tas_intermediate_steps = two_approx_solution(w, c, W)
    c2a = 2 * tas_total_val
    alpha = epsilon * c2a / n
    intermediate_steps += tas_intermediate_steps

    scaled_c = [math.floor(ci / alpha) for ci in c]
    max_scaled_c = sum(scaled_c)

    dp = [float("inf")] * (max_scaled_c + 1)
    dp[0] = 0
    parent = [-1] * (max_scaled_c + 1)
    item_taken = [-1] * (max_scaled_c + 1)
    for i in range(n):
        for value in range(max_scaled_c, scaled_c[i] - 1, -1):
            if dp[value - scaled_c[i]] + w[i] < dp[value]:
                dp[value] = dp[value - scaled_c[i]] + w[i]
                parent[value] = value - scaled_c[i]
                item_taken[value] = i
            intermediate_steps += 1

    result_value = max(value for value in range(max_scaled_c + 1) if dp[value] <= W)
    approximate_value = result_value * alpha

    result_items = [0] * n
    v = result_value
    while parent[v] != -1:
        result_items[item_taken[v]] = 1
        v = parent[v]

    total_weight = sum(w[i] for i in range(n) if result_items[i])

    return result_items, approximate_value, total_weight, intermediate_steps


__all__ = ["fptas_solution"]
