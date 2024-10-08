def unique_elements(nums):
    unique_set = set(nums)
    unique_list = list(unique_set) 
    return unique_list
test_cases = [
    [3, 7, 3, 5, 2, 5, 9, 2],      
    [-1, 2, -1, 3, 2, -2],         
    [1000000, 999999, 1000000]     
]
for i, input_array in enumerate(test_cases):
    result = unique_elements(input_array)
    print(f"Test case {i + 1} input: {input_array}, output: {result}")
