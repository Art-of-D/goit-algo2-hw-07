import random
import timeit
from functools import lru_cache
from LRU_cache import LRUCache


cache = LRUCache(1000)

def range_sum_no_cache(array, L, R):
    return sum(array[L:R + 1])


def update_no_cache(array, index, value):
    array[index] = value
  
def range_sum_with_cache(array, L, R):
    cache_key = (L, R)
    result = cache.get(cache_key)
    if result != -1:
        return result

    total_sum = sum(array[L:R + 1])
    cache.put(cache_key, total_sum)
    return total_sum
  

def update_with_cache(array, index, value):
    keys_to_delete = []
    for key in cache.get_keys():
        L, R = key
        if L <= index <= R:
            keys_to_delete.append(key)

    for key in keys_to_delete:
        cache.delete(key)

    array[index] = value


N = [random.randint(0, 100_000) for _ in range(100_000)]
Q = []
for _ in range(50_000):
    if random.choice(["Range", "Update"]) == "Range":
        L, R = sorted([random.randint(0, len(N) - 1) for _ in range(2)])
        Q.append(("Range", L, R))
    else:
        index = random.randint(0, len(N) - 1)
        value = random.randint(0, len(N) - 1)
        Q.append(("Update", index, value))


# Without cash
def no_cache_operations():
    for req in Q:
        if req[0] == "Range":
            range_sum_no_cache(N, req[1], req[2])
        else:
            update_no_cache(N, req[1], req[2])

# With cash
def cache_operations():
    for req in Q:
        if req[0] == "Range":
            range_sum_with_cache(N, req[1], req[2])
        else:
            update_with_cache(N, req[1], req[2])

# Вимірюємо час без кешування
time_no_cache = timeit.timeit(no_cache_operations, number=1)

# Вимірюємо час з кешуванням
time_with_cache = timeit.timeit(cache_operations, number=1)


print(f"Час виконання без кешування: {time_no_cache:.6f} секунд")
print(f"Час виконання з LRU-кешем: {time_with_cache:.6f} секунд")