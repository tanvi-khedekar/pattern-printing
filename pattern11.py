# Question 11: Hollow Right-Angled Triangle
# Expected output:

# *
# * *
# *   *
# *     *
# * * * * *

# Triangle is 5 lines tall
rows = 5

# Go through each row from top (1) to bottom (5)
for i in range(1, rows + 1):
    # Check each position across the current row up to 'i'
    for j in range(1, i + 1):
        # Print a star if we're on the left edge, the bottom row, or the slanted right edge
        if j == 1 or i == rows or j == i:
            print("*", end=" ")
        else:
            # Otherwise we're inside the triangle, so print a blank space
            print(" ", end=" ")
            
    # Done with this row, move to the next line
    print()