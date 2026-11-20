# The triangle is 5 lines tall
rows = 5

# Go through each line from 1 to 5
for i in range(1, rows + 1):
    # First, fill the left side with invisible blank spaces to push the stars to the right (fewer spaces as we go down)
    for space in range(rows - i):
        print(" ", end=" ")
        
    # Right after the spaces on the same line, print the stars for the current row
    for j in range(i):
        print("*", end=" ")
        
    # Move down to the next line once both spaces and stars are printed
    print()