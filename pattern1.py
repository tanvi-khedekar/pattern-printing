# Question 1: Solid Square
# Expected output:

# * * * *
# * * * *
# * * * *
# * * * *

rows = 4

for i in range(rows):         # outer loop: runs 4 times(for 4 rows)
  for j in range (rows):      # inner loop: prints 4 stars in single line
    print("*", end = " ")      
  print()                      # moves cursor to next line after finishing a row