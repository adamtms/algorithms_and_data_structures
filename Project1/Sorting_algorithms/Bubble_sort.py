def inputNumbers():
    return [int(x) for x in input().split()]

def bubbleSort(array):
    l = len(array)
    for i in range(1, l):
        for j in range(l-1, i-1, -1):
            if(array[j-1] > array[j]):
                array[j-1], array[j] = array[j], array[j-1]

if __name__ == '__main__':
    data = inputNumbers()
    bubbleSort(data)
    print(data)
