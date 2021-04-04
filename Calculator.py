# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

def calculator(num1, sign, num2):
    if sign == "+":
        return num1 + num2

    elif sign == "-":
        return num1 - num2

    elif sign == "*":
        return num1 * num2

    elif sign == "/":
        return num1 / num2

    elif sign == "%":
        return num1 % num2

    elif sign == "**":
        return num1 ** num2

    elif sign == "//":
        return num1 // num2


a = int(input("Enter 1st number : "))
b = input("Enter Operation : ")
c = int(input("Enter 2nd number : "))
print("Your answer is :", calculator(a, b, c))
