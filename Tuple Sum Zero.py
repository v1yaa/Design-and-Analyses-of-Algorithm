from collections import defaultdict
def four_sum_count(A, B, C, D):
    sum_map = defaultdict(int)
    for a in A:
        for b in B:
            sum_map[a + b] += 1
    count = 0
    for c in C:
        for d in D:
            target = -(c + d)
            if target in sum_map:
                count += sum_map[target]
    return count
A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
result = four_sum_count(A, B, C, D)
print(f"Number of tuples that sum to zero: {result}")
