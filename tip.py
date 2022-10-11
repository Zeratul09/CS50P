# This function gets the inputs and does the calculation when calling main at the end.
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


    # This function takes one argument it removes the currency sign and changes the number into a float.
def dollars_to_float(d):
    # TODO
    d = d.lstrip("$")
    d = float(d)
    return d


    # This function takes one argument it removes the percentage sign and changes the number to a float (also converting the percentage that was given).
def percent_to_float(p):
    # TODO
    p = p.rstrip("%")
    p = float(p)
    p = p / 100
    return p

main()