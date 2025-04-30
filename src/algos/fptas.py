import math
from typing import List
from .two_approx import two_approx_solution


def fptas_solution(w: List[int], c: List[int], W: int, epsilon: float = 0.1):
    n = len(w)
    intermediate_steps = 0

    _, c2a, _, tas_intermediate_steps = two_approx_solution(w, c, W)
    alpha = epsilon * 2 * c2a / n
    intermediate_steps += tas_intermediate_steps

    scaled_c = [math.floor(ci / alpha) for ci in c]
    sum_scaled_costs = sum(scaled_c)

    dp = [float("inf")] * (sum_scaled_costs + 1)
    dp[0] = 0
    parent = [-1] * (sum_scaled_costs + 1)
    item_taken = [-1] * (sum_scaled_costs + 1)
    for i in range(n):
        for cost in range(sum_scaled_costs, scaled_c[i] - 1, -1):
            if dp[cost - scaled_c[i]] + w[i] < dp[cost]:
                dp[cost] = dp[cost - scaled_c[i]] + w[i]
                parent[cost] = cost - scaled_c[i]
                item_taken[cost] = i
            intermediate_steps += 1

    scaled_cost_with_max_weight = max(cost for cost in range(sum_scaled_costs + 1) if dp[cost] <= W)
    result_cost = scaled_cost_with_max_weight * alpha

    result_items = [0] * n
    v = scaled_cost_with_max_weight
    while parent[v] != -1:
        result_items[item_taken[v]] = 1
        v = parent[v]

    total_weight = sum(w[i] for i in range(n) if result_items[i])

    return result_items, result_cost, total_weight, intermediate_steps


__all__ = ["fptas_solution"]
