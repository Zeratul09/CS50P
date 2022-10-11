#Getting and input and outputting the result.
def main():

    txt = input("Enter a number, aritthmetic expression and another number: ")
    print(calculator(txt))


#Character separator and calculator function:
def calculator(expression):

    x, y, z = expression.split(" ")

    x = int(x)
    y = y
    z = int(z)

    if y == "+":
        return float(x + z)
    elif y == "-":
        return float(x - z)
    elif y == "*":
        return float(x * z)
    else:
        return float(x / z)

main()