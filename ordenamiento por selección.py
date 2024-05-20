def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Ejemplo de uso
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array:", arr)
