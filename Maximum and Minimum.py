N = 8
a = [5, 7, 3, 4, 9, 12, 6, 2]
min_val = a[0]
max_val = a[0]
for i in range(1, N):
    if a[i] < min_val:
        min_val = a[i]
    if a[i] > max_val:
        max_val = a[i]
print("MIn=",min_val,"& Max=",max_val)
