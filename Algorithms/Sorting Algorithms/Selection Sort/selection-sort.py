def selectionSort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_elem_index = i

        # find minimum element's index
        for j in range(i + 1, n):   
            if arr[j] < arr[min_elem_index]:
                min_elem_index = j

        arr[i], arr[min_elem_index] = arr[min_elem_index], arr[i]
