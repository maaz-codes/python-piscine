import sys
import string


def main():
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        S = str(sys.argv[1])
        N = int(sys.argv[2])
        assert sum([c in string.punctuation for c in S]) == 0, "bad arguments"
        # for c in S:
        #     if c in string.punctuation:
        #         raise AssertionError("the arguments are bad")
        print((lambda S, N: [word for word in S.split(' ')
                             if len(word) > N])(S, N))
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except ValueError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
