# Simple Calculator 🔢

This is a simple calculator written in Python. It supports the following operations:

- Addition `+`
- Subtraction `-`
- Multiplication `*`
- Division `/`
- Power `**`

## How it works

The program runs in a loop and asks the user for an operation and two numbers, then performs the selected operation.

### Code:

```python
while True:  
    operation = input('Enter the operation: ')
    num1 = int(input('Enter number 1: '))
    num2 = int(input('Enter number 2: '))

    if operation == '+':
        def jam(a, b):
            return a + b
        print(jam(num1, num2))

    if operation == '-':
        def menha(a, b):
            return a - b
        print(menha(num1, num2))

    if operation == '*':
        def zarb(a, b):
            return a * b
        print(zarb(num1, num2))

    if operation == '/':
        def taghsim(a, b):
            if b == 0:
                return False
            else:
                return a / b
        print(taghsim(num1, num2))

    if operation == '**':
        def tavan(a, b):
            return a ** b
        print(tavan(num1, num2))
