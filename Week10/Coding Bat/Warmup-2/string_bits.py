def string_bits(str):
  a = ""
  n = len(str)
  for i in range(n):
    if i % 2 == 0:
      a = a + str[i]
  return a