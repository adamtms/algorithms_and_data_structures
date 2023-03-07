def insert_sort(array):
    length = len(array)
    for i in range(1, length):
        value = array[i]
        j = i
        while j > 0 and array[j-1] > value:
            array[j] = array[j-1]
            j -= 1
        array[j] = value