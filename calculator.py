calc = '''
/ ,-----------------. \
| |    1.05459 e -34| |
| `-----------------' |
| [@ ] On/Off  ###### |
|              ###### |
| [7] [8] [9] [C] [AC]|
|                     |
| [4] [5] [6] [X] [%] |
|                     |
| [1] [2] [3] [+] [-] |
|                     |
| [0] [.]  [EXP]  [=] |
\_____________________/

'''

print(calc)


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1 , n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("Enter the first number : "))
    print(" + \n - \n * \n /")
    operation_symbol = input("Pick an operation from the above line : ")
    num2 = float(input("Enter the second number : "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    return f"{num1} {operation_symbol} {num2} = {answer}"
    

answer1 = calculator()
print(answer1)

