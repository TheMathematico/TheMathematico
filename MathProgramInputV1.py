
AddSub = input("Addition, Subtraction, Multiplication or Division: ")
AddSubStr = str(AddSub)

SubtractList = [
    "subtraction",
    "Subtraction",
    "Subtract",
    "subtract",
    "minus",
    "subt",
    "sub",
    "-"
]

AdditionList = [
    "addition",
    "Addition",
    "add"
    "Add",
    "addi",
    "Addi",
    "lad",
    "+"
]

MultiplicationList = [
    "Multiplication",
    "multiplication",
    "multiply",
    "Multiply",
    "mult",
    "Mult",
    "mul",
    "Mul",
    "*",
    "x",
    "X"
]

DivisionList = [
    "division",
    "Division",
    "divide",
    "Divide",
    "divi",
    "Divi",
    "div",
    "Div",
    "/"
]


if AddSubStr in AdditionList:
    num1 = input("Num1: ")
    num2 = input("Num2: ")

    intNum1 = int(num1)
    intNum2 = int(num2)

    result = intNum1 + intNum2
    
    print(result)

elif AddSubStr in SubtractList:
    num1 = input("Num1: ")
    num2 = input("Num2: ")

    intNum1 = int(num1)
    intNum2 = int(num2)

    result = intNum1 - intNum2
    
    print(result)

elif AddSubStr in MultiplicationList:
    num1 = input("Num1: ")
    num2 = input("Num2: ")

    intNum1 = int(num1)
    intNum2 = int(num2)

    result = intNum1 * intNum2
    
    print(result)

elif AddSubStr in DivisionList:
    num1 = input("Num1: ")
    num2 = input("Num2: ")

    intNum1 = int(num1)
    intNum2 = int(num2)

    result = intNum1 / intNum2
    
    print(result)
else:
    print("invalid!")
