from typing import Any, Callable


def callLimit(limit: int) -> Callable:
    count = 0

    def callLimiter(function: Callable) -> Callable:
        def limit_function(*args: Any, **kwds: Any):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Function '{function}' call too many times")
        return limit_function
    return callLimiter
