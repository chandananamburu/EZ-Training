def print_pyramid(rows):
  for i in range(rows):

    for j in range(rows - i - 1):
      print(" ", end="")

    for j in range(i + 1):
      print("* ", end="")

    print()
print_pyramid(4)