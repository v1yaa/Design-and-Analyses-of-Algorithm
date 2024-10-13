array = [3, 9, 14, 19, 25, 31, 42, 47, 53]
search_key = 31
low = 0
high = len(array) - 1
comparisons = 0
while low <= high:
    mid = (low + high) // 2
    comparisons += 1 
    print(f"Comparing {search_key} with middle element {array[mid]} at index {mid}")
    if array[mid] == search_key:
        print(f"Element {search_key} found at index: {mid}")
        break
    elif array[mid] < search_key:
        low = mid + 1
    else:
        high = mid - 1
if low > high:
    print(f"Element {search_key} not found in the array.")
print(f"Total comparisons made: {comparisons}")
