answer = input("What is the the Great Question of Life, the Universe and Everything? ")

match answer:
    case "42" | "Forty-two" | "Forty two":
        print ("Yes")
    case _:
        print ("No")
        
