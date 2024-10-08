def find_maximum(nums):
    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num
    return max_value
test_cases = [
    [1, 2, 3, 4, 5],
    [7, 7, 7, 7, 7],
    [-10, 2, 3, -4, 5]
]
for i, input_array in enumerate(test_cases):
    result = find_maximum(input_array)
    print(f"Test case {i + 1} maximum: {result}")
