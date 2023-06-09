from generate import Instance
from brute import brute

def recursive(instance: Instance, actualPosition = 0, capacity = 0, value = 0, result = None) -> tuple[int, list[tuple[int]]]:
    if result == None:
        result = []

    if actualPosition == len(instance.items):
        return value, result

    excludedValue, excludedResult = recursive(instance, actualPosition+1, capacity, value, result.copy())

    includedValue = 0
    items = instance.items
    if capacity + items[actualPosition][0] <= instance.capacity:
        capacity += items[actualPosition][0]
        value += items[actualPosition][1]
        result.append(items[actualPosition])
        includedValue, includedResult = recursive(instance, actualPosition+1, capacity, value, result.copy())

    if includedValue > excludedValue:
        return includedValue, includedResult
    return excludedValue, excludedResult

if __name__ == "__main__":
    from generate import get_instance
    for i in range(20):
        inst = get_instance()
        value1, items1 = brute(inst)
        value2, items2 = recursive(inst)
        print(items2)
        print(inst.result_is_correct(items2))
        if value1 != value2:
            print("You fucked up")