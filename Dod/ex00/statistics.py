def ft_mean(data) -> float:
    '''this function calculates the mean of the data'''
    if not data:
        return
    return sum(data) / len(data)


def ft_median(data) -> float:
    '''this function calculates the median of the data'''
    if not data:
        return
    data.sort()
    n = len(data)
    if n % 2 == 0:
        return (data[n // 2 - 1] + data[n // 2]) / 2
    return data[n // 2]


def ft_quartile(data) -> list[float]:
    '''this function calculates the quartile of the data 25% and 75%'''

    if not data:
        return

    data.sort()
    n = len(data)

    def percentile(p):
        k = (n - 1) * p
        f = int(k)
        c = k - f
        if f + 1 < n:
            return data[f] + (data[f + 1] - data[f]) * c
        else:
            return data[f]

    q1 = percentile(0.25)
    q3 = percentile(0.75)

    return [q1, q3]


def ft_std(data) -> float:
    '''this function calculates the standard deviation of the data'''
    if not data:
        return
    mean = ft_mean(data)
    return (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5


def ft_var(data) -> float:
    '''this function calculates the variance of the data'''
    if not data:
        return
    mean = ft_mean(data)
    return sum((x - mean) ** 2 for x in data) / len(data)


def ft_statistics(*args: any, **kwargs: any) -> None:
    '''this function takes any number of arguments and keyword arguments'''
    try:
        data = list(args)
    except ValueError:
        print("ERROR")
        return
    # print(data)
    results = {}
    for key, value in kwargs.items():
        if value == "mean":
            results[value] = ft_mean(data)
        elif value == "median":
            results[value] = ft_median(data)
        elif value == "quartile":
            results[value] = ft_quartile(data)
        elif value == "std":
            results[value] = ft_std(data)
        elif value == "var":
            results[value] = ft_var(data)
        else:
            continue

    for key, result in results.items():
        if result is None:
            print("ERROR")
            continue
        print(f"{key} : {result}")
