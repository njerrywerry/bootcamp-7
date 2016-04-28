def find_max_min(arr):
  array = []
  max_, min_ = arr[0], arr[0]

  for i in arr:
    if i > max_:
      max_ = i
    if i < min_:
      min_ = i

  if min_ == max_:
    array.append(len(arr))
    return array
  else:
    array.append(min_), array.append(max_)
    return array
  
