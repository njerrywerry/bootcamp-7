def super_sum(*args):
    '''
    Returns a sum of numbers.
    e.g
        super_sum() ==> 0
        super_sum('string', 2, 3) ==> 0
        super_sum(1, 2, 3) ==> 6
        super_sum([10, 20, 30]) ==> 60
        super_sum([10], [20, 30]) ==> 60
    '''
    total = 0

    if args:
        for x in args:
            if type(x) == list:
                # same as total += sum(x)
                for i in x:
                    total += i
            elif type(x) == str:
                return 0
            else:
                total += x
        return total
    return 0
