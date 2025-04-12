import sys


def encoding_to_morse(text):
    '''this function Converts a text to morse code'''
    MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
        'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
        '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': '/'
    }
    for i in text:
        if i not in MORSE_CODE_DICT:
            raise AssertionError("the arguments are bad")
    return ' '.join(MORSE_CODE_DICT.get(i) for i in text)


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the argument are bad")

        txt = sys.argv[1].upper()
        morse = encoding_to_morse(txt)
        print(morse)

    except AssertionError as e:
        print(e)
