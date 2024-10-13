comparison_count = 0
def merge_sort(arr):
    global comparison_count
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            comparison_count += 1 
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
array = [12, 4, 78, 23, 45, 67, 89, 1]
print(f"Original array: {array}")
merge_sort(array)
print(f"Sorted array: {array}")
print(f"Number of comparisons: {comparison_count}")
