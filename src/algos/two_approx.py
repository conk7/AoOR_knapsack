from typing import List


def two_approx_solution(w: List[int], c: List[int], W: int):
    n = len(w)
    best_single_value = 0
    best_single_item = -1
    intermediate_steps = 0

    for i in range(n):
        if w[i] <= W and c[i] > best_single_value:
            best_single_value = c[i]
            best_single_item = i
        intermediate_steps += 1

    ratio_items = sorted(((c[i] / w[i], i) for i in range(n)), reverse=True)
    total_weight = 0
    total_value = 0
    chosen_items = []
    for _, i in ratio_items:
        if total_weight + w[i] <= W:
            total_weight += w[i]
            total_value += c[i]
            chosen_items.append(i)
        intermediate_steps += 1

    result_items = [0] * n
    if best_single_value >= total_value:
        if best_single_item != -1:
            result_items[best_single_item] = 1
        return (
            result_items,
            best_single_value,
            w[best_single_item] if best_single_item != -1 else 0,
            intermediate_steps,
        )
    else:
        for i in chosen_items:
            result_items[i] = 1
        return result_items, total_value, total_weight, intermediate_steps


__all__ = ["two_approx_solution"]
