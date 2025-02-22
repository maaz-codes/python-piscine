import sys
import string


def count_char_types(text: str):
    """
    Analyze a string and print counts of different character types.

    Parameters:
        text (str): The input string to analyze

    Returns:
        None: The function prints the results directly and does not return a value
    """
    total_len = len(text)
    upr_len = lwr_len = pun_len = sps_len = dgt_len = 0
    if (total_len > 0):
        for c in text:
            if c.isupper():
                upr_len += 1
            if c.islower():
                lwr_len += 1
            if (c in string.punctuation):
                pun_len += 1
            if (c.isspace()):
                sps_len += 1
            if (c.isdigit()):
                dgt_len += 1
        print(f"The text contains {total_len} character{'' if total_len == 1 else 's'}:")
        upr_len > 0 and print(f"{upr_len} upper letter{'' if upr_len == 1 else 's'}")
        lwr_len > 0 and print(f"{lwr_len} lower letter{'' if lwr_len == 1 else 's'}")
        pun_len > 0 and print(f"{pun_len} punctuation mark{'' if pun_len == 1 else 's'}")
        sps_len > 0 and print(f"{sps_len} space{'' if sps_len == 1 else 's'}")
        dgt_len > 0 and print(f"{dgt_len} digit{'' if dgt_len == 1 else 's'}")


def main():
    try:
        argc = len(sys.argv)
        assert argc <= 2, "more than one argument provided"
        if argc == 2 and len(sys.argv[1]):
            text = sys.argv[1]
        else:
            text = input("What is the text to count?\n")
        count_char_types(text)
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except (KeyboardInterrupt, EOFError):
        sys.exit()


if __name__ == "__main__":
    main()
