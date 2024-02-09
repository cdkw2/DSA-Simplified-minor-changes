def bubbleSort(arr):
    n = len(arr)
    for round in range(n):
        swapped = False
        for i in range(1, n - round):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swapped = True
        if not swapped:
            break