# Question 7: Star Pyramid
# Expected output:

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

# The pyramid has 5 rows in total
rows = 5

# Go through each row from top (row 1) to bottom (row 5)
for i in range(1, rows + 1):
    # First, print blank spaces on the left to push the stars toward the center
    for space in range(rows - i):
        print(" ", end=" ")
        
    # Next, print an odd number of stars (1, 3, 5, 7, 9) so the pyramid grows symmetrically on both sides
    for j in range(2 * i - 1):
        print("*", end=" ")
        
    # Move the cursor down to start the next row of the pyramid
    print()