# Question 2: Right-Angled Triangle
# Expected output:

# *
# * *
# * * *
# * * * *
# * * * * *


rows = 5

for i in range(1, rows + 1):      # outer loop: counts rows 1 to 5
  for j in range(i):          # Inner loop: runs 'i' times (Row 1 -> 1 star, Row 2 -> 2 stars, etc.)
    print("*", end = " ")
  print()