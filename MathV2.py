#This code is made in Python

import tkinter as tk   

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

def Num1Int():
    return int(Num1.get())

def Num2Int():
    return int(Num2.get())

def Submit_Function():
    symbol = Symbol.get()
    if symbol in AdditionList:
        result = Num1Int()+Num2Int()
    elif symbol in SubtractList:
        result = Num1Int()-Num2Int()
    elif symbol in MultiplicationList:
        result = Num1Int()*Num2Int()
    elif symbol in DivisionList:
        result = Num1Int()/Num2Int()
    else:
        result = "Invalid, consider using the symbols: +, -, /, *"
    User_Input.config(text=result)
    root.after(4000, clear_label)
    
def clear_label():
    User_Input.config(text="")

root =  tk.Tk()     
root.geometry("800x800") 
root.title("Test")     

Num1 =  tk.Entry(root)  
Num1.pack(padx=35, pady=50)

Symbol  = tk.Entry(root) 
Symbol.pack(padx=35, pady=60)

Num2  = tk.Entry(root)  
Num2.pack(padx=35, pady=55)

Submit = tk.Button(root, text="Submit?", command=Submit_Function)
Submit.pack(padx=35, pady=65)

User_Input = tk.Label(root, text="", font=("Arial", 24)) 
User_Input.pack(padx=35, pady=12)

root.mainloop()

