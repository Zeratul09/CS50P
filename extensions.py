#Input and print function:
def main ():

    file = input("File name?: ")
    print(detector(file))

#Searches and finds which one it matches:
def detector (text):

    text = text.casefold().lstrip(None).rstrip(None)
    
    if ".gif" in text:
        return "image/gif"
    elif ".jpg" in text:
        return "image/jpeg"
    elif ".jpeg" in text:
        return "image/jpeg"
    elif ".png" in text:
        return "image/png"
    elif ".pdf" in text:
        return "application/pdf"
    elif ".txt" in text:
        return "text/plain"
    elif ".zip" in text:
        return "application/zip"
    else:
        return "application/octet-stream"

main()