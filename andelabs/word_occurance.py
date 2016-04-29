def words(string):
  dict_ = {}

  for i in string.split():
      if i.isdigit():
          i = int(i)
      if i in dict_:
          dict_[i] += 1
      else:
          dict_[i] = 1
  return dict_
