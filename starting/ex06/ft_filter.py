def ft_filter(function, iterable) -> list:
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of
    iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    # i'm ussing list comprehension to filter the iterable
    if function is None:
        return [i for i in iterable if i]

    return [i for i in iterable if function(i)]


if __name__ == '__main__':
    print(ft_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
    print(ft_filter(None, [0, 1, 2, '', 'Hello', None, True, False]))
