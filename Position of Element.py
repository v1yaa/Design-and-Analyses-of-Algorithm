def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    comparisons = 0  
    while low <= high:
        comparisons += 1 
        mid = (low + high) // 2 
        if arr[mid] == key:
            return mid, comparisons  
        elif arr[mid] < key:
            low = mid + 1 
        else:
            high = mid - 1  
    return -1, comparisons  
if __name__ == "__main__":
    arr = [5, 10, 15, 20, 25, 30, 35, 40, 45]
    search_key = 20
    index, comparisons = binary_search(arr, search_key)
    if index != -1:
        print(f"Element {search_key} found at index {index}")
    else:
        print(f"Element {search_key} not found in the array")
    print(f"Number of comparisons made: {comparisons}")
