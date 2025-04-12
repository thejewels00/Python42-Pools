import sys
from ft_filter import ft_filter

if __name__ == "__main__":
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        s = sys.argv[1]
        try:
            n = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        result = ft_filter(lambda word: len(word) > n, s.split())

        print(list(result))
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
