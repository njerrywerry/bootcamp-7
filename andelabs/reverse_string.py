def reverse_string(string):
  reversed_string = ''

  if string == '':
    return None

  for x in range(len(string) - 1, -1, -1):
    reversed_string += string[x]

  if reversed_string == string:
    return True
  else:
    return reversed_string
