from generate import Instance
def greedy(instance: Instance) -> dict:
    sorted_items = sorted(instance.items, key=lambda x: x[1]/x[0], reverse=True)
    capacity = instance.capacity
    out_values = 0
    out_items = []
    for item in sorted_items:
        weight, value = item
        if weight <= capacity:
            capacity -= weight
            out_values += value
            out_items.append(item)
        else:
            break
    return out_values, out_items

if __name__ == "__main__":
    from generate import get_instance
    inst = get_instance()
    print(inst)
    print(greedy(inst))