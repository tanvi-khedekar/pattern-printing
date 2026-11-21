# Question 8: Inverted Star Pyramid
# Expected output:

# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

# Start with the widest row at the top (5 rows tall)
rows = 5

# Count backward from 5 down to 1 so the pyramid shrinks as we go down
for i in range(rows, 0, -1):
    # Print 0 spaces at the top, increasing by 1 each row down
    for space in range(rows - i):
        print(" ", end=" ")
        
    # Print shrinking odd numbers of stars (9, 7, 5, 3, 1) on the same line
    for j in range(2 * i - 1):
        print("*", end=" ")
        
    # move to the next line below
    print()