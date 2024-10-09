def find_kth_positive(arr, k):
    missing_count = 0  
    current_num = 1 
    index = 0 
    while missing_count < k:
        if index < len(arr) and arr[index] == current_num:
            index += 1 
        else:
            missing_count += 1  
        if missing_count == k:
            return current_num
        current_num += 1  
arr = [2, 3, 4, 7, 11]
k = 5
result = find_kth_positive(arr, k)
print(f"The {k}th missing positive number is: {result}")
