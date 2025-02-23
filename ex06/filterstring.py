import sys


def main():
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        S = str(sys.argv[1])
        N = int(sys.argv[2])
        print((lambda S, N: [word for word in S.split(' ') if len(word) > N])(S, N))
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except ValueError:
        print("AssertionError: the arguments are bad")

if __name__ == "__main__":
    main()
