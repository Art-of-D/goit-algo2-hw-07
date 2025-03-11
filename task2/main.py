from functools import lru_cache
from matplotlib import pyplot as plt
from splay_tree import SplayTree
import timeit

@lru_cache(maxsize=None)
def fibonacci_lru(n):
    if n <= 1:
      return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)

def fibonacci_splay(n, tree):
    if n <= 1:
      return n

    cache = tree.find(n)
    if cache is not None:
      return cache
    
    result = fibonacci_splay(n - 1, tree) + fibonacci_splay(n - 2, tree)
    tree.insert(n, result)
    return result


if __name__ == "__main__":
    array = [i for i in range (0, 950, 50)]
    tree = SplayTree()
    times_lru = []
    times_splay = []

    for i in array:
        time_lru = timeit.timeit(lambda: fibonacci_lru(i), number=1000)
        times_lru.append(time_lru)
        
        time_splay = timeit.timeit(lambda: fibonacci_splay(i, tree), number=1000)
        times_splay.append(time_splay)

    plt.figure(figsize=(10, 6))
    plt.plot(array, times_lru, label="LRU Cache", color="skyblue", marker="o")
    plt.plot(array, times_splay, label="Splay Tree", color="orange", marker="x")
    plt.title("Comparison of Fibonacci Calculation: LRU Cache vs Splay Tree")
    plt.xlabel("Fibonacci Number (n)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"{'n':<10}{'LRU Cache Time (s)':<25}{'Splay Tree Time (s)'}")
    print('-' * 50)
    for i, n in enumerate(array):
        print(f"{n:<10}{times_lru[i]:<25.8f}{times_splay[i]:.8f}")

