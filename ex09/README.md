# Maths Operations

## Overview

Maths Operations is a simple Python package that provides basic arithmetic and logical operations. This package is intended for demonstration purposes and serves as a template for structuring Python modules.

## Features

- Arithmetic Operations: Addition, subtraction, multiplication, and division.

- Logical Operations: AND and OR operations.

- Simple string-based outputs describing the performed operations.

## Installation

You can install this package using pip:
```bash
pip install git+https://github.com/maaz-codes/python-piscine.git@master#egg=maths_operations
```

Alternatively, clone the repository and install manually:
```bash
git clone https://github.com/maaz-codes/python-piscine.git
cd python-piscine/ex09/maths_op
pip install .
```

## Usage

### Arithmetic Operations
```bash
from maths_operation.arithmetic import add, subtract, multiply, divide
print(add(5, 3))         # Output: adding... 5 and 3
print(subtract(10, 4))  # Output: subtracting... 10 from 4
print(multiply(7, 2))    # Output: multiplying... 7 with 2
print(divide(8, 2))      # Output: dividing... 8 by 2
```

### Logical Operations
```bash
from maths_operation.logical import and_op, or_op

print(and_op(1, 0))  # Output: evaluating... 1 AND 0
print(or_op(1, 0))   # Output: evaluating... 1 OR 0
```

Project Structure
```bash
maths_operation/
├── __init__.py
├── arithmetic.py
└── logical.py
```

## Dependencies

This package requires:

- numpy>=1.21.0

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

### Maaz Khan

For any queries, reach out to maazkhan7454@gmail.com.

## Contributing

Feel free to fork the repository, create a feature branch, and submit a pull request!