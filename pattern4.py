# Question 4: Increasing Number Triangle
# Expected output:

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

rows = 5

for i in range(1, rows + 1):        # outer loop: controls the 5 rows
  for j in range(1, i + 1):         # Start counting from 1 up to the current row number and print each number side-by-side
    print(j, end = " ")
  print()           # press enter