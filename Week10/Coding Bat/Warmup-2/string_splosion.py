def string_splosion(str):
  a = ""
  for i in range(len(str)):
    a = a + str[:i+1]
  return a