import sys


def the_sums(str):
    '''This function takes a string as input and counts
      the number of upper case letters
     lower case letters, punctuation marks,
     spaces and digits in the string.
     It then prints the results.'''
    punctuations = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    print(sum(1 for c in str if c.isupper()), "upper letters")
    print(sum(1 for c in str if c.islower()), "lower letters")
    print(sum(1 for c in str if c in punctuations), "punctuation marks")
    print(str.count(' '), "spaces")
    print(sum(1 for c in str if c.isdigit()), "digits")


if __name__ == "__main__":
    '''This is the main function that calls the_sums function.'''
    try:
        len = len(sys.argv)
        assert len <= 2, "too many arguments"
        if len < 2:
            str = input("What is the text to count?\n")
        else:
            str = sys.argv[1]
        the_sums(str)

    except AssertionError as msg:

        print(f"Error: {msg}")
