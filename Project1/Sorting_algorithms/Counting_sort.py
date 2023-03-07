def counting_sort(array):
    max_value = max(array)
    output = [0] * len(array)
    counter = [0] * (max_value + 1)

    for i in array:
        counter[i] += 1

    for i in range(max_value):
        counter[i+1] += counter[i]

    for i in array:
        counter[i] -= 1
        output[counter[i]] = i

    return output