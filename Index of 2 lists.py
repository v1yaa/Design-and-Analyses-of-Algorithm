nums1 = [2, 3, 2]
nums2 = [1,2]
answer1 = 0
answer2 = 0
set_nums2 = set(nums2)
for num in nums1:
    if num in set_nums2:
        answer1 += 1
set_nums1 = set(nums1)
for num in nums2:
    if num in set_nums1:
        answer2 += 1
result = [answer1, answer2]
print(result)
