from generate import Instance
from itertools import combinations
def brute(instance: Instance) -> tuple[int, list[tuple[int]]]:
    items = instance.items
    max_capacity = instance.capacity
    best_comb = []
    best_value = 0
    for i in range(1, len(items)):
        for comb in combinations(items, i):
            total_value = 0
            total_cap_used = 0
            for weight, value in comb:
                total_value += value
                total_cap_used += weight
            if total_cap_used<=max_capacity and total_value>best_value:
                best_value = total_value
                best_comb = comb
    return best_value, best_comb

if __name__ == "__main__":
    from generate import get_instance
    inst = get_instance()
    print(inst)
    print(brute(inst))