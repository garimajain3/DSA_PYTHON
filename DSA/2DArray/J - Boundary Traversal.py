# 1. Get dimensions
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

ans = []

# Step 1: Top Row (Left to Right)
for j in range(m):
    ans.append(matrix[0][j])

# Step 2: Right Column (Top to Bottom)
# Start from index 1 to avoid the top-right corner we already grabbed
for i in range(1, n):
    ans.append(matrix[i][m-1])

# Step 3: Bottom Row (Right to Left)
# Check if n > 1 to ensure we aren't just repeating the Top Row
if n > 1:
    for j in range(m-2, -1, -1):
        ans.append(matrix[n-1][j])

# Step 4: Left Column (Bottom to Top)
# Check if m > 1 to ensure we aren't repeating the Right Column
if m > 1:
    for i in range(n-2, 0, -1):
        ans.append(matrix[i][0])

print(*(ans))