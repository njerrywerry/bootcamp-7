def find_missing(array1, array2):

    if array1 == [] and array2 == []:
        return 0
    elif cmp(array1, array2) == 0:
        return 0
    else:
        y = list(set(array1) ^ set(array2))
        return y[0]
