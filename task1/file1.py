def print_table(n):
  for i in range(1, n + 1):
    print("{} * {} = {}".format(i, 2, i * 2))

if __name__ == "__main__":
  print_table(10)
