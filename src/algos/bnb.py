import heapq
from typing import List


class Node:
    def __init__(self, level: int, cost: int, weight: int, taken: List[int]):
        self.level = level
        self.cost = cost
        self.weight = weight
        self.bound = 0
        self.taken = taken[:]

    def __lt__(self, other):
        return self.bound > other.bound


def bnb_solution(w: List[int], c: List[int], W: int):
    n = len(w)
    intermediate_steps = 0

    def compute_upper_bound(node: Node):
        intermediate_steps = 0
        if node.weight >= W:
            return 0, 0
        val_bound = node.cost
        total_weight = node.weight
        j = node.level
        while j < n and total_weight + w[j] <= W:
            total_weight += w[j]
            val_bound += c[j]
            j += 1
            intermediate_steps += 1
        if j < n:
            val_bound += (W - total_weight) * (c[j] / w[j])
        intermediate_steps += 1
        return val_bound, intermediate_steps

    items = sorted(
        [(w[i], c[i], i) for i in range(n)], key=lambda x: x[1] / x[0], reverse=True
    )
    w, c, indices = zip(*items)

    queue = []
    u = Node(0, 0, 0, [])
    u.bound, tmp_intermediate_steps = compute_upper_bound(u)
    intermediate_steps += tmp_intermediate_steps
    heapq.heappush(queue, u)
    intermediate_steps += 1

    max_cost = 0
    best_taken = []

    while queue:
        u: Node = heapq.heappop(queue)
        if not (u.bound > max_cost and u.level < n):
            continue

        taken_with = u.taken + [1]
        v = Node(u.level + 1, u.cost + c[u.level], u.weight + w[u.level], taken_with)
        if v.weight <= W and v.cost > max_cost:
            max_cost = v.cost
            best_taken = v.taken
        v.bound, tmp_intermediate_steps = compute_upper_bound(v)
        intermediate_steps += tmp_intermediate_steps
        if v.bound > max_cost:
            heapq.heappush(queue, v)

        taken_without = u.taken + [0]
        v = Node(u.level + 1, u.cost, u.weight, taken_without)
        v.bound, tmp_intermediate_steps = compute_upper_bound(v)
        intermediate_steps += tmp_intermediate_steps
        if v.bound > max_cost:
            heapq.heappush(queue, v)

        intermediate_steps += 2

    result_items = [0] * n
    for idx, take in enumerate(best_taken):
        if take:
            result_items[indices[idx]] = 1

    total_weight = sum(w[i] for i in range(n) if result_items[indices[i]])
    return result_items, max_cost, total_weight, intermediate_steps


__all__ = ["bnb_solution"]
