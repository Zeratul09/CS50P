# This code was made while learning Python by classroom course and by practicing coding in VSC.
# The name of the classroom course is: Harvard's CS50’s Introduction to Programming with Python.

# Pseudocode
#
# Begin -> need a convert and a main function.
# Input -> String :) or :( or anything else-
# Compute -> Convert the text if it's :) or :( to a 2d one otherwise nothing happens.
# Print -> The converted 2d picture or non matching text back to the user.

# Defining a main function

def main():
    
        # Get the input from the user.
        # You can define functions in the same identation.
        # Make sure you get an input at the end of the function.
        greeting = input("Type in either 'Hello :)' or 'Goodbye :(' or both at the same time: ")
        print(convert(greeting))

def convert(text):
    
        # Replace :) -> 🙂 or :( -> 🙁
        text = text.replace(":)", "🙂").replace(":(", "🙁")
        return text

main()
