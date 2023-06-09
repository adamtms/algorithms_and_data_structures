from generate import Instance
def dynamic(instance: Instance) -> int:
    num_items = instance.num_items
    capacity = instance.capacity
    array = [[0]*(capacity+1)]
    items = instance.items
    for weight, value in items:
        row = []
        for size in range(capacity + 1):
            if weight > size: 
                row.append(array[-1][size])
                continue
            row.append(max(array[-1][size], array[-1][size - weight] + value))
        array.append(row)

    rem = capacity
    res = array[num_items][capacity]
    result = []
    for i in range(num_items, 0, -1):
        if res <= 0:
            break
        if res == array[i - 1][rem]:
            continue
        else:
            weight, value = items[i - 1]
            result.append((weight, value))
            res = res - value
            rem = rem - weight

    return array[num_items][capacity], result

if __name__ == "__main__":
    from generate import get_instance
    inst = get_instance()
    print(inst)
    print(dynamic(inst))