def square(x: int | float) -> int | float:
    '''this function calculates the square of the number'''
    return x ** 2


def pow(x: int | float) -> int | float:
    '''this function calculates the power of the number'''
    return x ** x


def outer(x: int | float, function) -> object:
    count = 0

    def inner() -> float:
        nonlocal count, x
        x = function(x)
        return x

    # def inner() -> float:
    #     nonlocal count
    #     i = 0
    #     value = x
    #     while(True):
    #         value = function(value)
    #         if (i >= count):
    #             break
    #         i += 1
    #     count += 1
    #     return value

    return inner
