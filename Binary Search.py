arr = [3, 4, 6, -9, 10, 8, 9, 30]
arr.sort()
key = 10
low = 0
high = len(arr) - 1
found = False
position = -1
while low <= high:
    mid = (low + high) // 2  
    if arr[mid] == key:
        found = True
        position = mid
        break  
    elif arr[mid] < key:
        low = mid + 1  
    else:
        high = mid - 1  
print("Sorted array:", arr)
if found:
    print(f"Element {key} is found at position {position}.")
else:
    print(f"Element {key} is not found.")
