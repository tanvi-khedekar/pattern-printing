rows = 5

for i in range(rows, 0, -1):        # counts backwards from 5 to 1
  for j in range(i):            # prints i stars
    print("*", end = " ")
  print()