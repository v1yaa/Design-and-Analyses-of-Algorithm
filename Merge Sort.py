comparison_count = 0
def merge(arr, left, mid, right):
    global comparison_count
    L = arr[left:mid+1]
    R = arr[mid+1:right+1]
    i = 0 
    j = 0 
    k = left
    while i < len(L) and j < len(R):
        comparison_count += 1
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)
if __name__ == "__main__":
    N = 8
    arr = [12, 4, 78, 23, 45, 67, 89, 1]
    merge_sort(arr, 0, N-1)
    print(f"Sorted Array: {arr}")
    print(f"Number of comparisons: {comparison_count}")
