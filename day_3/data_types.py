def data_type(x):
    '''
    Takes in an argument, x:
        -for an integer, return x ** 2
        -for a float, return x / 2
        -for a string, return 'Hello ' + x
        -for a boolean, return 'boolean'
        -for a long, return 'long'
    '''

    if type(x) == int:
        return (x ** 2)
    elif type(x) == float:
        return (x / 2)
    elif type(x) == str:
        return 'Hello ' + x
    elif type(x) == bool:
        return 'boolean'
    elif type(x) == long:
        return 'long'
    else:
        return 'Invalid data type'

print data_type(7)
print data_type(4.0)
print data_type("Njeri")
print data_type(True)
print data_type(100 ** 100)
