#Input and printing out the result

def main():
    time = input("What time is it? ")
    print(convert(time))

def convert(time):

    #Format the string, pull the variables from it and calculate the decimal value:
    time.lower().lstrip().rstrip()
    hours, minutes = time.split(":")
    hours_f = float(hours)
    minutes_f = float(minutes.replace(" a.m.", "").replace(" p.m.", ""))/60
    decimal = hours_f + minutes_f

    #print(decimal, "decimal before") #Uncheck this comment to check the decimal value before conversion.
    
    #Convert to 12H to 24H if needed based on the input and modify the decimal number:
    if "a.m." in time and "12" in hours:
        decimal = decimal - 12
    elif "a.m" in time:
        decimal = decimal + 0
    elif "p.m." in time and "12" in hours:
        decimal = decimal - 12
    elif "p.m." in time:
        decimal = decimal + 12
    else: #The input was in already in 24H format:
        decimal + 0
    
    #print(decimal, "decimal after") #Uncheck this comment to check the decimal value after conversion.

    #Run the recalculated "decimal" variable and return the right answer:   
    if 7 <= decimal <= 8:
        return "breakfast time"
    elif 12 <= decimal <= 13:
        return "lunch time"
    elif 18 <= decimal <= 19:
        return "dinner time"
    else:
        return

if __name__ == "__main__":
    main()