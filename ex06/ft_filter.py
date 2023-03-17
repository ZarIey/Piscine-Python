def ft_filter(result, my_list):
    '''filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.'''

    return [x for x in my_list if (result(x) if result else x)]
