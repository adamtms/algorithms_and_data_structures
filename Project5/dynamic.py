from generate import Instance
def dynamic(instance: Instance) -> int:
    num_items = instance.num_items
    capacity = instance.capacity
    array = [[0]*(capacity+1)]
    for weight, value in instance.items:
        row = []
        for size in range(capacity + 1):
            if weight > size: 
                row.append(array[-1][size])
                continue
            row.append(max(array[-1][size], array[-1][size - weight] + value))
        array.append(row)
    return array[num_items][capacity], array

if __name__ == "__main__":
    from generate import get_instance
    inst = get_instance()
    print(inst)
    value, matrix = dynamic(inst)
    print(value, *matrix, sep="\n")