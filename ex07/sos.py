import sys


def morse_code_encoder(text: str) -> str:
    """
    Converts a text string into Morse code.
    """
    NESTED_MORSE = {
        'A': '.- ', 'B': '-... ', 'C': '-.-. ', 'D': '-.. ', 'E': '. ',
        'F': '..-. ', 'G': '--. ', 'H': '.... ', 'I': '.. ', 'J': '.--- ',
        'K': '-.- ', 'L': '.-.. ', 'M': '-- ', 'N': '-. ', 'O': '--- ',
        'P': '.--. ', 'Q': '--.- ', 'R': '.-. ', 'S': '... ', 'T': '- ',
        'U': '..- ', 'V': '...- ', 'W': '.-- ', 'X': '-..- ', 'Y': '-.-- ',
        'Z': '--.. ', ' ': '/ ',
        '0': '----- ', '1': '.---- ', '2': '..--- ', '3': '...-- ',
        '4': '....- ', '5': '..... ', '6': '-.... ', '7': '--... ',
        '8': '---.. ', '9': '----. ',
        }
    morse_code = ""
    for c in text.upper():
        if c not in NESTED_MORSE:
            raise ValueError(f"char {c} not present in morse.")
        morse_code += NESTED_MORSE[c]
    return morse_code


def main():
    try:
        assert (
            len(sys.argv) == 2 and
            sys.argv[1].replace(' ', '').isalnum()
        ), "the arguments are bad"
        print(morse_code_encoder(str(sys.argv[1])))
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")


if __name__ == "__main__":
    main()
