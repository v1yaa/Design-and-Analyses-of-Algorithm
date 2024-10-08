def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)
def partition(arr, low, high):
    pivot = arr[high]  
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1  
            arr[i], arr[j] = arr[j], arr[i]  
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
nums = [3, 4, 6, -9, 10, 8, 9, 30]
quicksort(nums, 0, len(nums) - 1)
print("Sorted array:", nums)
