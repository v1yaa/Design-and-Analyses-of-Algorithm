from itertools import combinations
def subset_sums(arr):
    n = len(arr)
    sums = []
    for i in range(n+1):
        for subset in combinations(arr, i):
            sums.append(sum(subset))
    return sums
def meet_in_the_middle(arr, target_sum):
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_sums = subset_sums(left_half)
    right_sums = subset_sums(right_half)
    right_sums_set = set(right_sums)
    for left_sum in left_sums:
        complement = target_sum - left_sum
        if complement in right_sums_set:
            return True
    return False
arr = [1, 3, 9, 2, 7, 12]
exact_sum = 15
result = meet_in_the_middle(arr, exact_sum)
print(f"Is there a subset that sums to {exact_sum}? {result}")
