# make repetition
# Tambah
def Tambah(n1,n2):
    return n1+n2

# kurang
def Kurang(n1,n2):
    return n1-n2
# kali
def Kali(n1,n2):
    return n1*n2
# bagi
def Bagi(n1,n2):
    return n1/n2

# create dictionary
operation = {
    "+" : Tambah,
    "*" : Kali,
    "/" : Bagi,
    "-" : Kurang
}



# looping operation
def calculator():
    # input
    num1 = input("provide the first number : ")
    if num1 == "":
        num1 = 0
    for symbol in operation:
        print(symbol)
    # add flag
    should_continue = True

    while should_continue:
        operation_symbol = input("pick an operation from the line above : " )
        num2 = int(input("provide the next number : "))
        calculation_function = operation[operation_symbol]
        first_answer = calculation_function(int(num1),num2)
        print(f"{num1} {operation_symbol} {num2} = {first_answer}")

        if input(f"type 'y' to countinue calculating with {first_answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = first_answer
        else:
            should_continue = False
            calculator()

calculator()

