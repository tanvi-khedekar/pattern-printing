# Question 12: Butterfly Pattern
# Expected output:

# *                 *
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *


# Half the height of the butterfly (5 rows up to the middle, 4 rows down)
rows = 5

# --- TOP HALF (Wings spreading outward: rows 1 to 5) ---
for i in range(1, rows + 1):
    # 1. Left wing: prints 'i' stars
    for j in range(i):
        print("*", end=" ")
        
    # 2. Empty gap in the middle: shrinks by 2 spaces every row down
    for space in range(2 * (rows - i)):
        print(" ", end=" ")
        
    # 3. Right wing: mirrors the left wing with 'i' stars
    for j in range(i):
        print("*", end=" ")
        
    # Move down to the next row
    print()

# --- BOTTOM HALF (Wings folding inward: rows 4 down to 1) ---
# Start at 4 so we don't repeat the solid 10-star middle line twice
for i in range(rows - 1, 0, -1):
    # 1. Left wing: shrinks from 4 stars down to 1
    for j in range(i):
        print("*", end=" ")
        
    # 2. Empty gap in the middle: widens by 2 spaces every row down
    for space in range(2 * (rows - i)):
        print(" ", end=" ")
        
    # 3. Right wing: shrinks from 4 stars down to 1
    for j in range(i):
        print("*", end=" ")
        
    # Move down to the next row
    print()