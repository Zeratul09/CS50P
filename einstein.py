# We need 1 input as a int
# We need to do 1 calculation
# We need to prin the result

# Input "m"
m = int(input(" Welcome to the Einstein's E = mc^2 calculator. \n" "Please enter a number for the mass (m) "))

def main():
    print(calculate())


# Calculate the numbers
def calculate():
    c = 300000000
    E = m * (pow(c, 2))
    return E

main()