import sys

def whatis(num: int) -> str:
    if num % 2 == 0:
        return "I'm Even."
    else:
        return "I'm Odd."

try:
    assert len(sys.argv) <= 2, "more than one argument is provided"
    try: 
        if len(sys.argv) == 2:
            num = int(sys.argv[1])
            print(whatis(int(sys.argv[1])))  
    except ValueError:
        raise AssertionError("argument is not an integer")
except AssertionError as e:
    print(f"AssertionError: {e}")
        