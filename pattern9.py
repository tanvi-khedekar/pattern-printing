# Question 9: Diamond
# Expected output:

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *


# Half the height of the diamond (from top tip to the widest middle line)
rows = 5

# --- TOP HALF (Normal Pyramid: rows 1 to 5) ---
for i in range(1, rows + 1):
    # Push the stars inward from the left so they center nicely
    for space in range(rows - i):
        print(" ", end=" ")
        
    # Print 1, 3, 5, 7, 9 stars as we move down
    for j in range(2 * i - 1):
        print("*", end=" ")
        
    # Done with this line, move down
    print()

# --- BOTTOM HALF (Upside-down Pyramid: rows 4 down to 1) ---
# Start at rows - 1 (which is 4) so we don't repeat the widest 9-star middle line
for i in range(rows - 1, 0, -1):
    # Add spaces back on the left as the triangle narrows
    for space in range(rows - i):
        print(" ", end=" ")
        
    # Print 7, 5, 3, 1 stars shrinking down to the bottom tip
    for j in range(2 * i - 1):
        print("*", end=" ")
        
    # Move down to the next line
    print()