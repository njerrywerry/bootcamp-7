def string_length(x):
  lengths = []

  if type(x) == str:
    lengths.append(len(x))
  elif type(x) == list:
    for i in x:
      lengths.append(len(i))

  return lengths
