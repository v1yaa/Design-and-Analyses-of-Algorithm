def process_numbers(nums):
    if not nums:
        return "The list is empty."
    sorted_nums = sorted(nums)
    return sorted_nums[-1]
test_cases = [
    [],           
    [5],         
    [3, 3, 3, 3] 
]
for i, input_array in enumerate(test_cases):
    result = process_numbers(input_array)
    print(f"Test case {i + 1} input: {input_array}, output: {result}")
