from pathlib import Path
from algos import (
    dp_solution,
    two_approx_solution,
    bnb_solution,
    fptas_solution,
)
from utils import measure_algorithm, print_results


BENCHMARKS_PATH = Path().resolve() / "benchmarks"
N = 1000


def main():
    for algo in [
        dp_solution,
        two_approx_solution,
        bnb_solution,
        fptas_solution,
    ]:
        benchmarks, avg_times, avg_steps, res_items, total_val, total_w = (
            measure_algorithm(algo, BENCHMARKS_PATH, N)
        )
        print_results(
            algo.__name__,
            benchmarks,
            avg_times,
            avg_steps,
            res_items,
            total_val,
            total_w,
        )


if __name__ == "__main__":
    main()
