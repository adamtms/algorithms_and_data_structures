def bubble_sort(array):
    l = len(array)
    for i in range(1, l):
        for j in range(l-1, i-1, -1):
            if(array[j-1] > array[j]):
                array[j-1], array[j] = array[j], array[j-1]
