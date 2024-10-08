nums = [3, 1, 2, 2, 2, 1, 3]
k = 2
index_map = {}
for index, value in enumerate(nums):
    if value not in index_map:
        index_map[value] = []
    index_map[value].append(index)
count = 0
for indices in index_map.values():
    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            if (indices[i] * indices[j]) % k == 0:
                count += 1
print(count)
