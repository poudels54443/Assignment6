import random
import time

def deterministic_select(arr, k):
    """
    Return the k-th smallest element (0-based) using the Median-of-Medians algorithm
    in worst-case linear time.
    """
    if not 0 <= k < len(arr):
        raise IndexError("k out of bounds")
    return _det_select(arr, k)

def _det_select(arr, k):
    n = len(arr)
    if n <= 5:
        return sorted(arr)[k]
    # Partition into groups of five
    groups = [arr[i:i+5] for i in range(0, n, 5)]
    # Find median of each group
    medians = [sorted(g)[len(g)//2] for g in groups]
    # Pivot is median of medians
    pivot = _det_select(medians, len(medians)//2)
    # Partition around pivot
    lows  = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    # Recurse into the correct partition
    if k < len(lows):
        return _det_select(lows, k)
    if k < len(lows) + len(pivots):
        return pivot
    return _det_select(highs, k - len(lows) - len(pivots))

def randomized_select(arr, k):
    """
    Return the k-th smallest element (0-based) using Quickselect
    in expected linear time.
    """
    if not 0 <= k < len(arr):
        raise IndexError("k out of bounds")
    return _rand_select(arr[:], k)

def _rand_select(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = random.choice(arr)
    lows  = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    if k < len(lows):
        return _rand_select(lows, k)
    if k < len(lows) + len(pivots):
        return pivot
    return _rand_select(highs, k - len(lows) - len(pivots))

def tests():
    """
    Compare running times of deterministic and randomized selection
    on various input sizes and distributions.
    """
    sizes = [1000, 5000, 10000]
    distributions = {
        'random': lambda n: [random.randint(0, n) for _ in range(n)],
        'sorted': lambda n: list(range(n)),
        'reverse': lambda n: list(range(n, 0, -1))
    }
    print(f"{'n':>6} | {'dist':>7} | {'det(ms)':>8} | {'rand(ms)':>9}")
    print("-" * 38)
    for n in sizes:
        for label, gen in distributions.items():
            data = gen(n)
            k = n // 2
            arr = data[:]
            t0 = time.perf_counter()
            deterministic_select(arr, k)
            t1 = time.perf_counter()
            randomized_select(arr, k)
            t2 = time.perf_counter()
            det_time = (t1 - t0) * 1000
            rand_time = (t2 - t1) * 1000
            print(f"{n:6} | {label:7} | {det_time:8.3f} | {rand_time:9.3f}")

if __name__ == "__main__":
    tests()
