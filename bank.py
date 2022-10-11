# In a file called bank.py, implement a program that prompts the user for a greeting. 
# If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. 
# Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.


#Main function that takes the input and will print the result:
def main():
    greeting = input("Greeting ")
    print(how_much_money(greeting))


# Formatting the input and checking it:
def how_much_money(str):
    
    str = str.casefold().lstrip(None).rstrip(None)
    
    if "hello" in str:
        return "$0"
    elif str.startswith('h'):
        return "$20"
    else:
        return "$100"
        

main()