# Question 10: Hollow Square
# Expected output:

# * * * * *
# *       *
# *       *
# *       *
# * * * * *

# Size of the square (5 rows tall, 5 columns wide)
size = 5

# Go through each row from top (1) to bottom (5)
for i in range(1, size + 1):
    # Check every spot across the row from left (1) to right (5)
    for j in range(1, size + 1):
        # Print a star ONLY if we are on the top, bottom, left, or right border
        if i == 1 or i == size or j == 1 or j == size:
            print("*", end=" ")
        else:
            # Otherwise, we're inside the box, so leave it blank
            print(" ", end=" ")
            
    # Finished checking all 5 spots in this row, jump to the next line
    print()