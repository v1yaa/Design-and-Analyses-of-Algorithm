def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
arr1 = [5, 2, 9, 1, 5, 6]
sorted_arr1 = selection_sort(arr1.copy())
print(f"Random Array: {arr1} -> Sorted Array: {sorted_arr1}")
arr2 = [10, 8, 6, 4, 2]
sorted_arr2 = selection_sort(arr2.copy())
print(f"Reverse Sorted Array: {arr2} -> Sorted Array: {sorted_arr2}")
arr3 = [1, 2, 3, 4, 5]
sorted_arr3 = selection_sort(arr3.copy())
print(f"Already Sorted Array: {arr3} -> Sorted Array: {sorted_arr3}")
