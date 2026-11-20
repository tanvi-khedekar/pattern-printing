# Question 5: Repeated Row Number Triangle
# Expected output:

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# We need 5 rows where each row repeats its own row number
rows = 5

# Move down through the rows, keeping track of which row 'i' we are currently on
for i in range(1, rows + 1):
    # Repeat the action 'i' times (e.g., on row 3, do this 3 times)
    for j in range(1, i + 1):
        # Print the current row number itself instead of counting up
        print(i, end=" ")
    # Move down to the next line when the row is complete
    print()