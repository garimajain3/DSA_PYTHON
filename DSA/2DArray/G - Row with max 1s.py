row, col = map(int, input().split())
matrics = []

for _ in range(row):
    current_row = [int(x) for x in input().split()]
    matrics.append(current_row)

max_ones = 0
result_index = -1  # Initialize it here!

for i in range(len(matrics)):
    count = 0
    for j in range(len(matrics[0])):
        if matrics[i][j] == 1:
            count += 1
            
    # Check if this row is the new leader
    if count > max_ones:
        max_ones = count
        result_index = i

# Now, even if no 1s were found, result_index exists and is -1
print(result_index)