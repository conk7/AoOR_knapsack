from pathlib import Path
import time
from typing import Callable, List


def measure_algorithm(algorithm: Callable, benchmarks_path: Path, n: int = 100):
    ws = []
    Ws = []
    ps = []

    answers = []

    for i in range(1, 8):
        Ws.append(int((benchmarks_path / f"{i}" / "W.txt").read_text()))
        ws.append(
            list(map(int, (benchmarks_path / f"{i}" / "w.txt").read_text().split(",")))
        )
        ps.append(
            list(map(int, (benchmarks_path / f"{i}" / "p.txt").read_text().split(",")))
        )
        answers.append(
            list(
                map(int, (benchmarks_path / f"{i}" / "ans.txt").read_text().split(","))
            )
        )

    # print(Ws)
    # print(ws)
    # print(ps)
    # print(answers)
    # print(list(zip(ws, ps, Ws, answers)))

    avg_times = []
    avg_steps = []
    res_items = []
    total_val = []
    total_w = []
    for w, p, W, ans in zip(ws, ps, Ws, answers):
        total_time = 0
        total_steps = 0

        result_items = 0
        total_value = 0
        total_weight = 0
        for _ in range(n):
            start = time.time()
            result_items, total_value, total_weight, intermediate_steps = algorithm(
                w, p, W
            )
            end = time.time()

            total_time += end - start
            total_steps += intermediate_steps

        res_items.append(result_items)
        total_val.append(total_value)
        total_w.append(total_weight)

        avg_time = total_time / n
        avg_time *= 1000

        avg_times.append(avg_time)
        avg_steps.append(total_steps // n)

    return list(range(1, 8)), avg_times, avg_steps, res_items, total_val, total_w


def print_results(
    algorithm: str,
    benchmarks: List[str],
    avg_times: List[float],
    avg_steps: List[int],
    res_items: List[float],
    total_val: List[float],
    total_w: List[float],
):
    print(f"\n\n{algorithm}")
    print(f"{'Benchmark':<15}{'Average time(ms)':<20}{'Num of steps':<15}{'Items (0-1)':<35}{'Price':<15}{'Weight':<15}")
    print("-" * 120)
    for f, t, s, i, v, w in zip(benchmarks, avg_times, avg_steps, res_items, total_val, total_w):
        print(f"{f:<15}{t:<20.4f}{s:<15}{' '.join(f'{x}' for x in i):<35}{v:<15.4f}{w:<15}")
