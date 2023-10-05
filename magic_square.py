def magic_square(n):
  """Generates a magic square of size n x n.

  Args:
    n: The size of the magic square.

  Returns:
    A list of lists representing the magic square.
  """

  # Create an empty magic square.
  magic_square = [[0 for i in range(n)] for j in range(n)]

  # Initialize the current position to the middle of the top row.
  i = n // 2
  j = n - 1

  # Recursively fill the magic square.
  _fill_magic_square(magic_square, i, j, 1)

  return magic_square


def _fill_magic_square(magic_square, i, j, num):
  """Recursively fills a magic square.

  Args:
    magic_square: A list of lists representing the magic square.
    i: The current row index.
    j: The current column index.
    num: The next number to be placed in the magic square.
  """

  # If we have reached the end of the magic square, we are done.
  if num > len(magic_square)**2:
    return

  # Try to place the next number in the magic square.
  if magic_square[i][j] == 0:
    magic_square[i][j] = num
  else:
    # If the current position is already occupied, try to place the next
    # number in a different position.
    _fill_magic_square(magic_square, (i + 1) % len(magic_square),(j - 2) % len(magic_square), num)

  # Recursively fill the rest of the magic square.
  _fill_magic_square(magic_square, (i - 1) % len(magic_square),(j + 1) % len(magic_square), num + 1)


if __name__ == '__main__':
  # Generate a 3x3 magic square.
  magic_square = magic_square(3)

  # Print the magic square.
  for row in magic_square:
    print(' '.join(map(str, row)))
