n = int(input())

# Create a list to store the strings so we can mirror them easily
rows = []

for i in range(n):
    if i == 0:
        # The very first row is just the character
        rows.append(">")
    else:
        # Indent + Char + Middle Spaces + Char
        leading = " " * i
        middle = " " * (2 * i - 1)
        rows.append(f"{leading}>{middle}>")

# Print the top half (including the widest point)
for row in rows:
    print(row)

# Print the bottom half (everything except the last row of 'rows', in reverse)
for row in reversed(rows[:-1]):
    print(row)